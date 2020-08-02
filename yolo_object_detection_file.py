import cv2
import numpy as np
import location_file
import io
import os
# Load Yolo

class Yolo_object_detection:
    def __init__(self):
        self.net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
        self.classes = []
        with open("coco.names", "r") as f:
            self.classes = [line.strip() for line in f.readlines()]
        self.layer_names = self.net.getLayerNames()
        self.output_layers = [self.layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
        self.colors = np.random.uniform(0, 255, size=(len(self.classes), 3))
        self.location = location_file.Location()


    def detect_objects(self,img):
        # Loading image
        img = cv2.resize(img, None, fx=0.4, fy=0.4)
        height, width, channels = img.shape

        # Detecting objects
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

        self.net.setInput(blob)
        outs = self.net.forward(self.output_layers)
        # Showing informations on the screen
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.7:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    pos = self.location.getXLoc(detection[0])
                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h,pos])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        font = cv2.FONT_HERSHEY_PLAIN
        # objects = []
        obj_dict = dict()
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h, pos = boxes[i]
                label = str(self.classes[class_ids[i]])
                # objects.append([label,pos])
                obj_dict[label] = obj_dict.get(label,list())
                obj_dict[label].append(pos)
                color = self.colors[class_ids[i]]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (x, y + 30), font, 3, color, 3)


        return obj_dict

# yolo_object_detection = Yolo_object_detection()
# # with io.open(os.path.join('room_ser.jpg'), 'rb') as image_file:
# #             content = image_file.read()
# image = cv2.imread('abc.jpeg')

# print(yolo_object_detection.detect_objects(image))