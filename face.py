#Author : Megha Saxena
#Video link for explaination :https://drive.google.com/file/d/1Zot-LLyom_0oywuGRVEyvJ9IFtLF7Un4/view?usp=sharing
import cv2
import numpy as np
import face_recognition
import os
import streamlit as st

st.title("Who are you??")
#Connecting to camera
run = st.checkbox('Run')

FRAME_WINDOW = st.image([])

#To keep the image name
path = 'images'
images = []
#Collecting Name
personName = []

#List of all our images
myList = os.listdir(path)
#Print all names of the images
# print(myList)

#cu_img will take values from the list
for cu_img in myList:
    current_img = cv2.imread(f'{path}/{cu_img}')
    images.append(current_img)
    personName.append(os.path.splitext(cu_img)[0])
# print(personName)

def faceEncodings(images):
    encodeList = []
    for img in images:
        #Convert images to black and white
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = faceEncodings(images)
print("All Encodings Completed!!!")

#This is to get access to laptop camera
#The value of VideoCapture is 0 for laptop camera and 1 for external camera
camera = cv2.VideoCapture(0)

while run:
    ret, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #Resizing face
    faces = cv2.resize(frame, (0,0), None, 0.25, 0.25)
    faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

    #To find faces in camera frame
    facesCurrentFrame = face_recognition.face_locations(faces)
    encodeCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)


    for encodeFace, faceLoc in zip(encodeCurrentFrame, facesCurrentFrame):
        #For matching faces
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        #For face distance
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = personName[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(frame, (x1,y1),(x2,y2),(0,255,0), 2)
            cv2.rectangle(frame, (x1, y2-35), (x2,y2), (0,255,0), cv2.FILLED)
            cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    FRAME_WINDOW.image(frame)

else:
    st.write('Stopped')