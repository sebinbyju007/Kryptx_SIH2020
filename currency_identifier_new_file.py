import io
import os
from google.cloud import vision
from google.cloud.vision import types
import numpy as np
import pandas as pd
import math

class CurrencyIdentifier:

    def __init__(self):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'sih-demo-273507-07035952879b.json'
        self.client = vision.ImageAnnotatorClient()

    def detect_text(self):
        with io.open(os.path.join('image.jpg'), 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)
        response = self.client.document_text_detection(image=image)
        document = response.full_text_annotation
        words=list()
        for page in document.pages:
            for block in page.blocks:
                for paragraph in block.paragraphs:
                    for word in paragraph.words:
                        k = ''
                        for symbol in word.symbols:
                            k=k+k.join(str(symbol.text))
                    
                        # k=k+k.join(' ')
                        words.append(k)
                    # k=k+k.join('\n')
        print(words)
        return words


    def identify_currency(self):
            words = self.detect_text()
            if '2000' in words:
                return '2000 Rupees Note'
            elif '500' in words:
                return '500 Rupees Note'
            elif '200' in words:
                return '200 Rupees Note'
            elif '100' in words:
                return '100 Rupees Note'
            elif '50' in words:
                return '50 Rupees Note'
            elif '20' in words:
                return '20 Rupees Note'
            elif '10' in words:
                return '10 Rupees Note'
            else:
                return 'Currency Not Clear'


# currencyIdentifier = CurrencyIdentifier()
# print(currencyIdentifier.identify_currency())

