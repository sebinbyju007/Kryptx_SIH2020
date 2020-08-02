import io
import os
from google.cloud import vision
from google.cloud.vision import types

class FullTextDetection:

    def __init__(self):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'
        self.client = vision.ImageAnnotatorClient()

    def detectText(self):
        with io.open(os.path.join('image.jpg'), 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)
        response = self.client.document_text_detection(image=image)
        document = response.full_text_annotation
        k=''
        for page in document.pages:
            for block in page.blocks:
                for paragraph in block.paragraphs:
                    for word in paragraph.words:
                        for symbol in word.symbols:
                            k=k+k.join(str(symbol.text))
                        k=k+k.join(' ')
                    k=k+k.join('\n')

        return k



