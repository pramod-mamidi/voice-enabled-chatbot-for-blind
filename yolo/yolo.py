import cv2 as cv
import numpy as np
import time
import keyboard
import pyttsx3
import subprocess
def spawn_program_and_die(program, exit_code=0):
    subprocess.Popen(program)
    sys.exit(exit_code)
def SpeakText(command):
    engine = pyttsx3.init()
    engine.getProperty('rate')
    engine.setProperty('rate',160)
    engine.say(command)
    engine.runAndWait()
WHITE = (255, 255, 255)
img = None
img0 = None
outputs = None
# Load names of classes and get random colors
classes = open(r'C:/Users/MAMIDICRAO/Desktop/half/yolo/coco.names').read().strip().split('\n')
np.random.seed(42)
colors = np.random.randint(0, 255, size=(len(classes), 3), dtype='uint8')

# Give the configuration and weight files for the model and load the network.
net = cv.dnn.readNetFromDarknet(r'C:/Users/MAMIDICRAO/Desktop/half/yolo/yolov3.cfg', r'C:/Users/MAMIDICRAO/Desktop/half/yolo/yolov3.weights')
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
# net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

# determine the output layer
ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

def load_image():
    cap=cv.VideoCapture(0)
    while(1):
        ret, frame = cap.read()
        frame=cv.flip(frame,1)
        global img, img0, outputs, ln
        blob = cv.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)
        t0 = time.time()
        outputs = net.forward(ln)
        t = time.time() - t0
        outputs = np.vstack(outputs)
        if keyboard.is_pressed('q'):
            SpeakText("going back")
            spawn_program_and_die(['python','home2.py'])
        else:
            post_process(frame, outputs, 0.5)
        cv.imshow('window',  frame)
        # if cv.waitKey(1) & 0xFF == ord('a'):
        #     SpeakText("going back")
        #     spawn_program_and_die(['python','home2.py'])

def post_process(img, outputs, conf):
    H, W = img.shape[:2]

    boxes = []
    confidences = []
    classIDs = []

    for output in outputs:
        scores = output[5:]
        classID = np.argmax(scores)
        confidence = scores[classID]
        if confidence > conf:
            x, y, w, h = output[:4] * np.array([W, H, W, H])
            p0 = int(x - w//2), int(y - h//2)
            p1 = int(x + w//2), int(y + h//2)
            boxes.append([*p0, int(w), int(h)])
            confidences.append(float(confidence))
            classIDs.append(classID)
            # cv.rectangle(img, p0, p1, WHITE, 1)

    indices = cv.dnn.NMSBoxes(boxes, confidences, conf, conf-0.1)
    if len(indices) > 0:
        for i in indices.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            color = [int(c) for c in colors[classIDs[i]]]
            cv.rectangle(img, (x, y), (x + w, y + h), color, 2)
            text = "{}: {:.4f}".format(classes[classIDs[i]], confidences[i])
            SpeakText(text+'percent')
            cv.putText(img, text, (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

def trackbar(x):
    global img
    conf = x/100
    img = img0.copy()
    post_process(img, outputs, conf)
    cv.displayOverlay('window', f'confidence level={conf}')
    cv.imshow('window', img)
cv.namedWindow('window')
cv.createTrackbar('confidence', 'window', 50, 100, trackbar)
load_image()
