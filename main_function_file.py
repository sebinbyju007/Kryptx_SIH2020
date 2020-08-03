import cv2
import yolo_object_detection_file
import largest_text_detection_file
# import currency_detection_file
import full_text_detection_file
import currency_identifier_new_file
import sign_board_detection_file
import medicine_remainder_file
import medicine_detection_file
import face_detection_file
class MainFunction:
    def __init__(self):
        self.yolo_object_detection = yolo_object_detection_file.Yolo_object_detection()
        self.faceDetection = face_detection_file.FaceDetection()
        # self.q = list()
        self.largestTextDetection = largest_text_detection_file.LargestTextDetection()
        # self.currencyClassifier = currency_detection_file.Currency_Classifier()
        self.currencyIdentifier = currency_identifier_new_file.CurrencyIdentifier()
        self.fullTextDetection = full_text_detection_file.FullTextDetection()
        self.signBoardDetection = sign_board_detection_file.SignBoardDetection()
        self.medicineDetection = medicine_detection_file.MedicineDetection()


    

    def main_function(self,frame,val):
        img = frame
        obj_arr = []
        pos_arr = []

        if val == 3:
            cv2.imwrite('image.jpg',img)
            try:
                return self.largestTextDetection.detect_largest_text()
            except :
                return 'No Text Found or Image not clear'

        elif val == 2:
            cv2.imwrite('image.jpg',img)
            try:
                return self.currencyIdentifier.identify_currency()
            except:
                return 'No text Found or Image Not Clear'

        elif val == 1:
                cv2.imwrite('image.jpg',img)
                try:
                    return self.fullTextDetection.detectText()
                except :
                    return 'No text Found or Image Not Clear'
        elif val== 4:
            cv2.imwrite('image.jpg')
            try:
                return self.signBoardDetection.classify('image.jpg')
            except:
                return 'No signal Found or Image Not Clear'

        elif val == 6:
            cv2.imwrite('image.jpg',img)
            try:
                return self.medicineDetection.detect_largest_text()+' tablet'
            except :
                return 'No text Found or Image Not Clear'
        
        elif val == 5:
            try:
                return medicine_remainder_file.alarmTrigger()
            except:
                return 'No output'
        elif val == 7:
            return 'Good Night Royal , Sweet Dreams, Bye'

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
                if k=='person':
                    continue
                # if len(self.q)>=0:
                #     self.q.pop(0)
                # self.q.append(k)
                if not val :
                    output_text = 'There is a - '
                    val = True
                for pos in v:
                    output_text+=k+' - '+pos+'. '
                    # output_text=output_text.join(pos+' ')
                    
            


            if 'person' in objects.keys():
                #  and 'person' not in self.q
                # print(self.q)
                cv2.imwrite('image.jpg',frame)
                person,emmotion = self.faceDetection.face_detection()
                # if len(person)>=1:
                #     self.q.append('person')

                for p,e in zip(person,emmotion):
                    output_text+=p+'-'+e+'. '


                


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
# image = cv2.imread('modiji.jpg')
# mainFun = MainFunction()
# print(mainFun.main_function(image,0))


