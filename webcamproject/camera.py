import cv2
import numpy as np

facec = cv2.CascadeClassifier('static/classifiers/haarcascade_frontalface_default.xml')
font=cv2.FONT_HERSHEY_SIMPLEX

class VideoCamera(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        _,fr=self.video.read()
        gray_fr=cv2.cvtColor(fr,cv2.COLOR_BGR2GRAY)
        faces=facec.detectMultiScale(gray_fr,1.4,1)

        for(x,y,w,h) in faces:
            fc=gray_fr[y:y+h,x:x+w]
            cv2.rectangle(fr,(x,y),(x+w,y+h),(0,255,0),2)

        _,jpeg=cv2.imencode('.jpg',fr)
        return jpeg.tobytes()
