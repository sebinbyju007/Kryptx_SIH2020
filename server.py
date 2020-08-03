import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new
import zlib
import pyttsx3
import main_function_file


engine = pyttsx3.init()
engine.setProperty('rate',100)
engine.setProperty('voice',engine.getProperty('voices')[1].id)

HOST=''
PORT=8485
mainFunction = main_function_file.MainFunction()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')
engine.say('Started')
engine.runAndWait()
conn,addr=s.accept()
variable = True
data = b""
payload_size = struct.calcsize(">L")
print("payload_size: {}".format(payload_size))
while True:
    try:
        while len(data) < payload_size:
            print("Recv: {}".format(len(data)))
            # if len(data)==0:
            #     raise Exception('Client connection loss')
            data += conn.recv(4096)
        print("Done Recv: {}".format(len(data)))
        if variable:
            engine.say('Good Morning Royal')
            engine.runAndWait()
            variable = False
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack(">L", packed_msg_size)[0]
        print("msg_size: {}".format(msg_size))
        while len(data) < msg_size:
            data += conn.recv(4096)
        frame_data = data[:msg_size]
        data = data[msg_size:]

        frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
        print('value  is '+str(frame['value']))
        val = frame['value']
        image = cv2.imdecode(frame['image'], cv2.IMREAD_COLOR)
        cv2.imshow('window',image)
        # try:
        output_text = mainFunction.main_function(image,val)
        print(output_text)
        engine.say(output_text)
        engine.runAndWait()
        # except :
        #     print('bad image')
        data_new=b'"hai"'
        conn.sendall(data_new)
    except :
        print('client connection loss')
        sys.exit()
