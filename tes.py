import pytesseract
import cv2
from PIL import Image
import subprocess
import sys
import pyttsx3
def spawn_program_and_die(program, exit_code=0):
    subprocess.Popen(program)
    sys.exit(exit_code)
def SpeakText(command):
    engine = pyttsx3.init()
    engine.getProperty('rate')
    engine.setProperty('rate',160)
    engine.say(command)
    engine.runAndWait()
def main_t():
    # Use the attached camera to capture images
    # 0 stands for the first one
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        text = pytesseract.image_to_string(Image.fromarray(img1))
        print("Extracted Text: ", text)
        SpeakText(text)
        cv2.imshow('frame', img1)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            SpeakText("going back")
            spawn_program_and_die(['python','home2.py'])
    cap.release()
main_t()
