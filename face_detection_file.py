import face_recognition
from PIL import Image, ImageDraw
import os, sys, io
import glob
from google.cloud import vision
import numpy as np
import pandas as pd

class FaceDetection:

    def check_fun(self,matches,files,draw,pil_image,left,right,bottom,top):
        if True in matches:
            first_match_index = matches.index(True)
            name = files[first_match_index].split('\\')[1].split('.')[0]
            draw.rectangle(((left,top),(right,bottom)),outline=(0,0,0))

            text_width,text_height = draw.textsize(name)

            draw.rectangle(((left ,bottom ),(right, bottom)),fill= (0,0,0),outline=(0,0,0))

            draw.text((left ,bottom - text_height ),name, fill=(255,255,255))

            return name

        else:
            name = str(input("Enter the name"))
            pil_image.save("./img/known/{0}.jpg".format(name)) 
            return name


    def emmotion(self,unknown_image_location):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'sih-demo-273507-07035952879b.json'

        client = vision.ImageAnnotatorClient()

        with io.open(unknown_image_location,'rb') as image_file:
            content = image_file.read()

        image_to_find_face_details = vision.types.Image(content = content)

        response = client.face_detection(image = image_to_find_face_details)

        face_annotation = response.face_annotations

        face_emotion = [' is infront of you with a cheerful face',' is infront of you with a with sorrow face',' is infront of you with an angery face',' is infront of you with a surprise',' is infront of you with a underexposed face',' is infront of you with a blurred face',' is infront of you with a headwear']

        emmotion_of_person = list()
        for face in face_annotation:
                b = [face.joy_likelihood,
                        face.sorrow_likelihood,
                        face.anger_likelihood,
                        face.surprise_likelihood,
                        face.under_exposed_likelihood,
                        face.blurred_likelihood,
                        face.headwear_likelihood]
                emmotion_of_person.append(face_emotion[b.index(max(b))])

        return emmotion_of_person


    def face_detection(self):
        img_dir = "./img/known/" 
        data_path = os.path.join(img_dir,'*.jpg')
        files = glob.glob(data_path)
        data = []

        for f1 in files:
            img = face_recognition.load_image_file(f1)
            data.append(face_recognition.face_encodings(img)[0])

        unknown_image_location = './image.jpg'

        test_image = face_recognition.load_image_file(unknown_image_location)

        face_location = face_recognition.face_locations(test_image)
        face_encodings = face_recognition.face_encodings(test_image,face_location)

        pil_image = Image.fromarray(test_image)

        draw = ImageDraw.Draw(pil_image)

        matches = []
        name_of_person = []
        for (top,bottom,left,right) , face_encoding in zip(face_location,face_encodings):
            matches = face_recognition.compare_faces(data,face_encoding)
            print(matches)
            name_of_person.append(self.check_fun(matches,files,draw,pil_image,top,bottom,left,right))

        emmotion_of_person=self.emmotion(unknown_image_location)

        return name_of_person,emmotion_of_person


# faceDetection = FaceDetection()
# print(faceDetection.face_detection())
