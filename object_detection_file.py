import os, io
from google.cloud import vision
import numpy as np
import pandas as pd
import math
import location_file




def object_detection():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'
    client = vision.ImageAnnotatorClient()

    bounds = []
    with io.open('image.jpg', 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.object_localization(image=image, retry=False)
    frame = pd.DataFrame(
        columns=['object', 'confidence', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4', 'centreX', 'centreY', 'xLoc',
                 'yLoc'])

    obj_detail = list()
    location = location_file.Location()
    for loc_obj in response.localized_object_annotations:
        obj_detail.clear()
        for vertex in loc_obj.bounding_poly.normalized_vertices:
            obj_detail.append(vertex.x)
            obj_detail.append(vertex.y)
        frame_dict = dict(object=loc_obj.name,
                          confidence=loc_obj.score,
                          x1=obj_detail[0],
                          y1=obj_detail[1],
                          x2=obj_detail[2],
                          y2=obj_detail[3],
                          x3=obj_detail[4],
                          y3=obj_detail[5],
                          x4=obj_detail[6],
                          y4=obj_detail[7],
                          centreX=(obj_detail[0] + obj_detail[4]) / 2,
                          centreY=(obj_detail[1] + obj_detail[5]) / 2
                          )
        loc_dict = dict(xLoc=location.getXLoc(frame_dict.get('centreX')),
                        yLoc=location.getYLoc(frame_dict.get('centreY')))
        frame_dict.update(loc_dict)
        frame = frame.append(frame_dict, ignore_index=True)
    return frame