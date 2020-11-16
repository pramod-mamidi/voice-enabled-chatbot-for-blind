import pandas
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications import resnet50
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
import matplotlib.pyplot as plt
import cv2
import os
import bot
import pyttsx3
import subprocess
import sys
lis=['Hundred','Two Hundred','Thousand','Five Hundred','Fifty','ten','twenty']
mod=bot.mod
def spawn_program_and_die(program, exit_code=0):
    subprocess.Popen(program)
    sys.exit(exit_code)
def SpeakText(command):
    engine = pyttsx3.init()
    engine.getProperty('rate')
    engine.setProperty('rate',160)
    engine.say(command)
    engine.runAndWait()
cap = cv2.VideoCapture(0)
while cap.isOpened():
       ret, frame = cap.read()
       img1 = frame
       imgr=cv2.resize(img1, (224,224),interpolation = cv2.INTER_NEAREST)
       imgr=imgr.reshape(-1,224,224,3)
       pred=mod.predict(imgr)
       predl=pred.tolist()
       l=predl.index(max(predl))
       SpeakText(lis[l])
       cv2.imshow('frame', img1)
       if cv2.waitKey(0) & 0xFF == ord('q'):
           SpeakText("going back")
           spawn_program_and_die(['python','home2.py'])
cap.release()
