import cv2
import io
import socket
import struct
import time
import sys
import pickle
import zlib
import speech_recognition as sr
from threading import Thread
import pyaudio
#import google.cloud.vision as vision
from pynput.keyboard import Listener


value=0
Run=1

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.43.39', 8485))
connection = client_socket.makefile('wb')

# cam.set(3, 1200)
# cam.set(4, 1200)

img_counter = 0

def on_press(key):
    global value
    if hasattr(key,'char'):
        if key.char == 'c': 
            speech()
        elif  key.char == 'q':
            client_socket.close()
            cam.release()
            return False

    print(value)
    

def speech():
    print('Say Something')
    global value
    r = sr.Recognizer()
    print('hai')
    mic = sr.Microphone()
    with mic as source:
        audio = r.listen(soucrce,phrase_time_limit=5)
        text = ''
        
        try:
            text = r.recognize_google(audio)
            print(text)
            a=text.split(' ')
            if 'read' in a:
                value=1
                print("value is %d"%value)
            elif 'currency' in a:
                value=2
                print("value is %d"%value) 
            elif 'identify' in a:
                value=3
                print("value is %d"%value)
            elif 'medicine' in a:
                value = 6
                print("value is %d"%value)
            elif 'good night' in a:
                value = 7
                print("value is %d"%value)
            elif 'sign board' in a:
                value = 4
                print("value is %d"%value)

        except sr.RequestError:
            print('RequestError')
        except sr.UnknownValueError:
            print('UnknownValueError')

        

def camera(client_socket,Run):
    img_counter=0
    global value
    while Run==1:
        try:
            cam = cv2.VideoCapture(0)
            ret, frame = cam.read()
            result, frame = cv2.imencode('.jpg', frame, encode_param)
        #    data = zlib.compress(pickle.dumps(frame, 0)
            k={'image':frame,'value':value}
            data = pickle.dumps(k)
            size = len(data)

            print("{}: {}".format(img_counter, size))
            client_socket.sendall(struct.pack(">L", size) + data)
            img_counter += 1
            value=0
            data_new=client_socket.recv(10)
            print("{!r}".format(data_new))
            cam.release()
            time.sleep(3.0)
        except:
            print('Connection loss')
        

        


encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

camera_thread=Thread(target=camera,args=(client_socket,Run))
camera_thread.start()
try:
    with Listener(on_press = on_press) as listener:
        listener.join()
except EOFError:
    print("Error")   
# camera(cam,client_socket,Run)
