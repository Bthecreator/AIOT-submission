# Importing the needed libraries, please install them if there is an error
# Note: The model may struggle to detect if a person is wearing a mask, idk why :(
import cv2
import time
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import pyfirmata

board = pyfirmata.Arduino('COM3') #Replace COM3 with the name of the port the arduino is connected with if there is an error

cap = cv2.VideoCapture(0) #Starts capturing video input
cap.set(3, 640)
cap.set(4, 480)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
maskClassifier = load_model('./Model.h5') #Loads the model

while True:
   
    _, frame = cap.read()

    if not _:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        )
    
    for (x, y, h, w) in faces:

        faceROI = frame[y : y + h, x : x + w, :]

        faceROI = cv2.resize(faceROI, (160, 160)) #rescaling video input
        faceROI = img_to_array(faceROI) #converting the captured image into an array for processing
        faceROI = faceROI.reshape(1, 160, 160, 3) #Turing the image into a tensor

        prediction = maskClassifier(faceROI)
        (withoutmask, withmask) = prediction[0].numpy() #predicting...


        (label, color, prob) = ('Mask', (0, 255, 0), withmask*100.0) if withmask > withoutmask else ('No mask', (0, 0, 255), withoutmask*100.0) #outputting through a text label

        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

        cv2.rectangle(frame, (x + 15, y + 2), (x + w - 15, y + 20), (0, 0, 0), -1) #lower
        cv2.rectangle(frame, (x + 15, y - 2), (x + w - 15, y - 20), (0, 0, 0), -1) #upper

        cv2.putText(frame, str(prob)+' %', (x + 20, y - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
        cv2.putText(frame, label, (x + 20, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)

        
    cv2.imshow('Video', frame)

    if withoutmask > withmask: # Outputting through an arduino
            board.digital[2].write(1)
    else:
        board.digital[2].write(0)

    if cv2.waitKey(1) & 0xff == ord('q'): #Q to close the program
        break

cap.release()
cv2.destroyAllWindows()
