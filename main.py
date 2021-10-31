import tkinter 
from tkinter import *
from tkinter import messagebox
import cv2
import numpy as np
from keras.preprocessing import image
import warnings
warnings.filterwarnings("ignore")
from keras.preprocessing.image import load_img, img_to_array 
from keras.models import  load_model
import matplotlib.pyplot as plt
import numpy as np
import random

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Tkinter Login Form - pythonexamples.org')

# load model
model = load_model("best_model.h5")
face_haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

def scanButton():
    messagebox.showinfo( title = "Look at the Camera", message= "Look at the Camera\nOnce the facial expression is labeled, press Q to stop scanning!")
    while True:
        f = open("emotions.txt", "w")
        ret, test_img = cap.read()  # captures frame and returns boolean value and captured image
        if not ret:
            continue
        gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)

        faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)

        for (x, y, w, h) in faces_detected:
            cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=6)
            roi_gray = gray_img[y:y + w, x:x + h]  # cropping region of interest i.e. face area from  image
            roi_gray = cv2.resize(roi_gray, (224, 224))
            img_pixels = image.img_to_array(roi_gray)
            img_pixels = np.expand_dims(img_pixels, axis=0)
            img_pixels /= 255

            predictions = model.predict(img_pixels)

            # find max indexed arra y
            max_index = np.argmax(predictions[0])

            emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
            predicted_emotion = emotions[max_index]
            f.write(emotions[max_index] + "\n")
            cv2.putText(test_img, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        resized_img = cv2.resize(test_img, (1000, 700))
        cv2.imshow('Facial emotion analysis ', resized_img)
        if cv2.waitKey(10) == ord('q'):  # wait until 'q' key is pressed
            f.close()
            break
    messagebox.showinfo( title = '', message= "Scanning Completed")
    cap.release()
    cv2.destroyAllWindows

def read():
    # Random number for random quotes
    x = random.randint(1,4)
    # Opens file containing emotion from scanning
    y = open("emotions.txt", "rt")
    # Reads the first 11 characters
    z = y.read(10)
    # Strips the first 11 characters, so its only text
    emotion = z.strip()
    print(z)
    if emotion == "angry":
        quote = open("angry.txt", "rt")
        messagebox.showinfo( title = '', message= quote.readlines(x))
    else if emotion == disgust
    else:
        messagebox.showinfo( title = '', message= 'You have not scanned your facial expression yet!')
    

quitButton = tkinter.Button(tkWindow, 
                   text="Quit", 
                   fg="red",
                   command=quit)

#login button
scan = Button(tkWindow, text="Scan", command = scanButton)
msgButton = Button(tkWindow, text="Mesage", command = read)
scan.pack()
msgButton.pack()
quitButton.pack()

tkWindow.mainloop()