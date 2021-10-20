import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

#1. Paint img a certain colour
# blank[:] = 0,0,255
# cv.imshow('Green', blank)

#2. Draw a Rectangle
# cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)

#3. Draw a Circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
# cv.imshow('Circle', blank)

#4. Draw a Line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
# cv.imshow('Line', blank)

#5. Write Text on Image
cv.putText(blank, 'You were hacked by CrzyF', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Trojanhorse.exe', blank)

cv.waitKey(0)