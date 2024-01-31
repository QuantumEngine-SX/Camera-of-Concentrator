import cv2 as cv
import numpy as numpy
import sys
import numpy as np


s = 0 
if len(sys.argv)>1:
    s = sys.argv[1]

cap = cv.VideoCapture(s)

win_name = 'Camera Preview'
cv.namedWindow(win_name,cv.WINDOW_NORMAL)

while True:

    _,frame = cap.read()

    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    lower_white = np.array([0,0,255])
    upper_white = np.array([255,255,255])

    mask = cv.inRange(hsv,lower_white,upper_white)

    res = cv.bitwise_and(frame,frame,mask= mask)

    cv.imshow(win_name,frame)
    cv.imshow("mask",mask)
    cv.imshow('res',res)

    key = cv.waitKey(10)
    if (key == ord('q')):
        break

cv.destroyAllWindows()
