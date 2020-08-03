from datetime import datetime
import pickle
import json
from threading import Thread
import time
import pyttsx3



engine = pyttsx3.init()
engine.setProperty('rate',100)
engine.setProperty('voice',engine.getProperty('voices')[1].id)


def second_converter(time,a):
    return int(time.split(a)[0][1:])*3600+int(time.split(a)[1][:-1])*60

def add_medicine():
    med_dict={'15_38':'Zincovit'}
    file_a=open('medicine.json','w')
    json.dump(med_dict,file_a)
    file_a.close()

def medicine_rema():
    while True:
        a_file=open('medicine.json','r')
        a=a_file.read()
        print(a)
        key,value=a[1:-1].split(':')
        print(key,value)
        total_seconds=second_converter(key,'_')
        print(total_seconds)
        time_now="\""+str(datetime.now().strftime('%H:%M'))+"\""
        print(time_now)
        time_now=second_converter(time_now,':')
        print(time_now)
        rem_time=time_now-total_seconds
        print(rem_time)
        if abs(rem_time)<100:
            s="Its time to consume %s."%value
            engine.say(s)
            engine.runAndWait()
            return 0
        else:
            time.sleep(abs(rem_time))

thread=Thread(target=medicine_rema,args=())
thread.start()


def alarmTrigger():
    return 'Its time to consume Zincovit Tablet'