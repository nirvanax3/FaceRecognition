import cv2
import os
import pickle

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/background.png')

#Importing the mode images into a list
folderModePath ='Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for modePath in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, modePath)))

#Load the encoding file
file = open("EncodeFile.p",'rb')
encodeListKnownWithIDs = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIDs
print(studentIds)


while True:
    success, img = cap.read()

    imgBackground[162:162 + 480,55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[0]


#Import the encoding file


#Load the encoding file
file = open("EncodeFile.p",'rb')
encodeListKnown = pickle.load(file)

#cv2.imshow("Webcam",img)
cv2.imshow("Face Attendance",imgBackground)
cv2.waitKey(1)