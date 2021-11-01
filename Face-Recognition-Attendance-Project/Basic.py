import cv2
import numpy as np
import face_recognition
#step-1:BGR2RGB
imgvirat=face_recognition.load_image_file('virat.jpg')
imgvirat=cv2.cvtColor(imgvirat,cv2.COLOR_BGR2RGB)

imgdhoni=face_recognition.load_image_file('Dhoni.jpg')
imgdhoni=cv2.cvtColor(imgdhoni,cv2.COLOR_BGR2RGB)

imgtest=face_recognition.load_image_file('virat-test.jpg')
imgtest=cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)

# step-2:finding faces in the image

faceLoc=face_recognition.face_locations(imgvirat)[0]
encodeVirat=face_recognition.face_encodings(imgvirat)[0]


faceLoc1=face_recognition.face_locations(imgdhoni)[0]
encodedhoni=face_recognition.face_encodings(imgdhoni)[0]
#print(type(faceLoc))-->It returns a tuple with four values in it.

cv2.rectangle(imgvirat,(faceLoc[1],faceLoc[2]),(faceLoc[3],faceLoc[0]),(255,20,60),2)
cv2.rectangle(imgdhoni,(faceLoc1[1],faceLoc1[2]),(faceLoc1[3],faceLoc1[0]),(255,20,60),2)
faceLoctest=face_recognition.face_locations(imgtest)[0]
encodetest=face_recognition.face_encodings(imgtest)[0]





cv2.rectangle(imgtest,(faceLoctest[1],faceLoctest[2]),(faceLoctest[3],faceLoctest[0]),(255,0,255),2)



#step-3:Comparing the faces and finding the distance between them.
#and uses linearsvm to  find the match
#128 encodings are obtained

results = face_recognition.compare_faces([encodeVirat],encodetest)
#The lower the face_distance,perfect is the match.
facedis=face_recognition.face_distance([encodeVirat],encodetest)

results1 = face_recognition.compare_faces([encodedhoni],encodetest)

facedis1=face_recognition.face_distance([encodedhoni],encodetest)
print(results,facedis)

cv2.putText(imgtest,f'{results} {round(facedis[0],2)}',(20,50),cv2.FONT_HERSHEY_TRIPLEX,1,(0,255,255),1)

cv2.imshow('Virat Kohli',imgvirat)
cv2.imshow('Dhoni',imgdhoni)
cv2.imshow('Virat test',imgtest)
cv2.waitKey(0)
