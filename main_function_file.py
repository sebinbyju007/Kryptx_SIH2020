import cv2
import yolo_object_detection_file
import full_text_detection_file
class MainFunction:
    def __init__(self):
        self.yolo_object_detection = yolo_object_detection_file.Yolo_object_detection()
        # self.q = list()
        self.fullTextDetection = full_text_detection_file.FullTextDetection()


    

    def main_function(self,frame,val):
        img = frame
        obj_arr = []
        pos_arr = []

        

        if val == 1:
                cv2.imwrite('image.jpg',img)
                try:
                    return self.fullTextDetection.detectText()
                except :
                    return 'No text Found or Image Not Clear'
        
        else:

            # objects = self.yolo_object_detection.detect_objects(frame)
            # for object in objects:
            #     if object[0] not in self.q:
            #         obj_arr.append(object[0])
            #         pos_arr.append(object[1])
            #         if q.full():
            #             q.get()
            #         q.put(object[0])
                
                    



            # if 'person' in obj_arr.keys():
            #     cv2.imwrite('image.jpg',img)
            #     result_face_detection = self.faceDetection.face_detection()
            #     obj_arr.remove(index)
            #     pos_arr.remove(index)
            #     for i,j in result_face_detection:
            #         obj_arr.append(i)
            #         pos_arr.append(j)
            #     # print(result_face_detection)
            output_text =' '
            objects = self.yolo_object_detection.detect_objects(frame)
            # if len(objects)>0 :
            #     output_text = ''
            print(objects)
            dic = {}
            val=False
            for k,v in objects.items():
                # if k in self.q :
                #     continue
                # else:
                #     dic[k] = v
                # if k=='person':
                #     continue
                # if len(self.q)>=0:
                #     self.q.pop(0)
                # self.q.append(k)
                if not val :
                    output_text = 'There is a - '
                    val = True
                for pos in v:
                    output_text+=k+' - '+pos+'. '
                    # output_text=output_text.join(pos+' ')
                    

                


            return output_text


# image2 = cv2.imread('room_ser.jpg')
# print(mainFunction.main_function(image2,0))
# image3 = cv2.imread('0.jpg')
# print(mainFunction.main_function(image3,0))
# image1 = cv2.imread('bdroom.jpg')
# print(mainFunction.main_function(image1,0))
# image2 = cv2.imread('room_ser.jpg')
# print(mainFunction.main_function(image2,0))
# image3 = cv2.imread('0.jpg')
# print(mainFunction.main_function(image3,0))
# image = cv2.imread('large_text.jpeg')
# print(mainFunction.main_function(image,1))
# image = cv2.imread('image.jpg')
# mainFun = MainFunction()
# print(mainFun.main_function(image,0))


