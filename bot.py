from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr
import tensorflow as tf
from tensorflow import keras
import pyttsx3
import spacy
import subprocess
import sys
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests as r
import time
import keyboard
mod=tf.keras.models.load_model('save_model')
r = sr.Recognizer()
i=1
def spawn_program_and_die(program, exit_code=0):
    subprocess.Popen(program)
    sys.exit(exit_code)
def SpeakText(command):
    engine = pyttsx3.init()
    engine.getProperty('rate')
    engine.setProperty('rate',160)
    engine.say(command)
    engine.runAndWait()
def bot_start(chatbot):
    c=0
    while(True):
        if c==1:
            spawn_program_and_die(['python','error_page.py'])
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                print(MyText)
                if("object recog" in MyText):
                    SpeakText("enabling object detector")
                    from yolo import yolo
                    print("opening object detection")
                elif("play song" in MyText):
                    SpeakText("opening song player")
                    global n
                    n=(MyText[10:])
                    import play_song
                elif("read text" in MyText):
                    SpeakText("opening text reader")
                    import tes
                elif("currency" in MyText):
                    SpeakText("opening Currency Detector")
                    import pred_test
                elif(MyText=="bye"):
                    exit()
                else:
                    response = chatbot.get_response(MyText)
                    print(response)
                    SpeakText(str(response))

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            c+=1
            print("unknown error occured")
