import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Test for using camera by openCV
'''
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''

# Test for smoothing by GaussianBlur
'''
while(True):
    t0 = cap.read()[1]
    grey1 =  cv2.cvtColor(t0, cv2.COLOR_BGR2GRAY)
    blur1 = cv2.GaussianBlur(grey1,(7,7),0)
    cv2.imshow('frame', t0)
    cv2.imshow('grey', grey1)
    cv2.imshow('blur', blur1)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
'''

# Test for background subtraction.
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
    #print(fgmask)

    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
