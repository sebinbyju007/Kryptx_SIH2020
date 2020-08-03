import argparse
from enum import Enum
import io
import os
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw
import numpy as np
import pandas as pd
import math



class MedicineDetection:
    def __init__(self):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'sih-demo-273507-07035952879b.json'

        self.client = vision.ImageAnnotatorClient()

    def detect_largest_text(self):

        bounds = []

        with io.open(os.path.join('image.jpg'), 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = self.client.document_text_detection(image=image)
        document = response.full_text_annotation
        frame = pd.DataFrame(columns=['x1','y1','x2','y2','x3','y3','x4','y4','area','text']) 

        x1=0
        x2=0
        x3=0
        x4=0
        y1=0
        y2=0
        y3=0
        y4=0
        text=''
        for page in document.pages:
                for block in page.blocks:
                    for paragraph in block.paragraphs:
                        x1=paragraph.words[0].symbols[0].bounding_box.vertices[0].x
                        x2=paragraph.words[0].symbols[0].bounding_box.vertices[1].x
                        x3=paragraph.words[0].symbols[0].bounding_box.vertices[2].x
                        x4=paragraph.words[0].symbols[0].bounding_box.vertices[3].x
                        y1=paragraph.words[0].symbols[0].bounding_box.vertices[0].y
                        y2=paragraph.words[0].symbols[0].bounding_box.vertices[1].y
                        y3=paragraph.words[0].symbols[0].bounding_box.vertices[2].y
                        y4=paragraph.words[0].symbols[0].bounding_box.vertices[3].y
                        area=math.sqrt((x2-x1)**2+(y2-y1)**2)*math.sqrt((x3-x2)**2+(y3-y2)**2)
                        for word in paragraph.words:
                            for symbol in word.symbols:
                                text+=text.join(symbol.text)
                            text+=text.join(' ')
                        frame=frame.append(dict(x1=x1,
                                        x2=x2,
                                        x3=x3,
                                        x4=x4,
                                        y1=y1,
                                        y2=y2,
                                        y3=y3,
                                        y4=y4,
                                        area=area,
                                        text = text),ignore_index=True)
                        text=''

        return(list((frame[frame['area']==max(frame['area'])]['text']))[0])


# largestTextDetection = LargestTextDetection()
# largestTextDetection.detect_largest_text()
