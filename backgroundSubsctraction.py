import numpy as np
import cv2

MOVEMENT_THRESHOLD = 50
ACCUMULATE_THRESHOLD = 5

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()
count = 0


# main function
while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)[9:210,149:350]
    cv2.rectangle(frame, (10,150), (210,350), (100,100,100), 3)
    #print(fgmask)
    #print(np.average(fgmask))
    if(np.average(fgmask) >= MOVEMENT_THRESHOLD):
        count += 1
        print(count)
        if(count >= ACCUMULATE_THRESHOLD):
            print("succeed")
            count = 0
            # do something
            frame = cap.read()[1]

    cv2.imshow('frame',frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
