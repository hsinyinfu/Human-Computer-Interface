import numpy as np
import cv2
import time

MOVEMENT_THRESHOLD = 50
ACCUMULATE_THRESHOLD = 8
#COMMAND_RECTANGLE = [[(10,50),(210,250)], [(10,350),(210,550)]]
COMMAND_RECTANGLE = [[(10,50),(210,250)]]

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()
count = np.zeros((1, len(COMMAND_RECTANGLE)))
startTime = None
photoCount = 0
font = cv2.FONT_HERSHEY_SIMPLEX

# points: [ [(10,50),(210,250)], [(10,350),(210,550)]... ]
def createCommandRectangle(frame, points):
    fgmask = list()
    originFrame = np.copy(frame)
    for recPoints in points:
        leftUpX, leftUpY = recPoints[0]
        rightDownX, rightDownY = recPoints[1]
        #fgmask.append(fgbg.apply(np.copy(originFrame))[leftUpX:rightDownX,leftUpY:rightDownY])
        test = fgbg.apply(np.copy(originFrame))[leftUpX:rightDownX,leftUpY:rightDownY]
        fgmask.append(test)
        cv2.rectangle(frame, (leftUpX, leftUpY), (rightDownX, rightDownY),\
                (100,100,100), 3)
    return (frame, fgmask)

def countDown(passTime):
    global frame, font
    if passTime >= 4:
        return -1
    elif passTime >= 3:
        #print(3)
        cv2.putText(frame,'1',(10,500), font,5,(255,255,255),2,cv2.LINE_AA)
    elif passTime >= 2:
        #print(2)
        cv2.putText(frame,'2',(10,500), font,5,(255,255,255),2,cv2.LINE_AA)
    else:
        #print(1)
        cv2.putText(frame,'3',(10,500), font,5,(255,255,255),2,cv2.LINE_AA)


def takePicture():
    global startTime, frame, photoCount
    while True:
        waited = time.time() - startTime
        if countDown(waited) == -1:
            break
        cv2.imshow('frame',frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        frame = cap.read()[1]
    photo = cap.read()[1]
    photoCount += 1
    cv2.imwrite('photo-'+str(photoCount)+'.jpg',photo)
'''
def recordVideo():
    global startTime, frame, cap, ret
    while True:
        waited = time.time() - startTime
        if countDown(waited) == -1:
            break
        cv2.imshow('frame',frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        ret, frame = cap.read()
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',-1, 20.0, (640,480))
    startTime = time.time()
    
    while(time.time()-startTime <= 3):
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.flip(frame,180)

            # write the flipped frame
            out.write(frame)

            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    out.release()
'''

def executeCommand(num):
    if num == 0:
        takePicture()
    #elif num == 1:
        #recordVideo()
    else:
        print(error)

# main function
while(1):
    ret, frame = cap.read()
    #fgmask = fgbg.apply(frame)[9:210,149:350]
    #cv2.rectangle(frame, (10,150), (210,350), (100,100,100), 3)
    frame, fgmask = createCommandRectangle(frame, COMMAND_RECTANGLE)
    #frame, fgmask = createCommandRectangle(frame, [[(10,150),(210,350)]])


    #print(fgmask)
    #print(np.average(fgmask))
    for i in range(len(fgmask)):
        if(np.average(fgmask[i]) >= MOVEMENT_THRESHOLD):
            count[0,i] += 1
            #print(count[0,:])
            if(int(count[0,i]) >= ACCUMULATE_THRESHOLD):
                #print("succeed")
                #print('i=' + str(i))
                count[0,i] = 0
                startTime = time.time()
                executeCommand(i)
                #takePicture()
                frame = cap.read()[1]

    cv2.imshow('frame',frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

