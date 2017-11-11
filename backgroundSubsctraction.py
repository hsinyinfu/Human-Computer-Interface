import numpy as np
import cv2
import time

MOVEMENT_THRESHOLD = 50
ACCUMULATE_THRESHOLD = 5

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()
count = 0
startTime = None
photoCount = 0
font = cv2.FONT_HERSHEY_SIMPLEX

def takePicture():
    global startTime, frame, font, photoCount
    while True:
        waited = time.time() - startTime
        if waited >= 4:
            break
        elif waited >= 3:
            #print(3)
            cv2.putText(frame,'1',(10,500), font,5,(255,255,255),2,cv2.LINE_AA)
        elif waited >= 2:
            #print(2)
            cv2.putText(frame,'2',(10,500), font,5,(255,255,255),2,cv2.LINE_AA)
        else:
            #print(1)
            cv2.putText(frame,'3',(10,500), font,5,(255,255,255),2,cv2.LINE_AA)
        cv2.imshow('frame',frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        frame = cap.read()[1]
    photo = cap.read()[1]
    photoCount += 1
    cv2.imwrite('photo-'+str(photoCount)+'.jpg',photo)

# main function
while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)[9:210,149:350]
    cv2.rectangle(frame, (10,150), (210,350), (100,100,100), 3)
    #print(fgmask)
    #print(np.average(fgmask))
    if(np.average(fgmask) >= MOVEMENT_THRESHOLD):
        count += 1
        #print(count)
        if(count >= ACCUMULATE_THRESHOLD):
            #print("succeed")
            count = 0
            startTime = time.time()
            takePicture()
            frame = cap.read()[1]

    cv2.imshow('frame',frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

