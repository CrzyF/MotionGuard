import cv2 as cv

img = cv.imread('photos/cat.jpeg')

cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    #Images, Videos and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions=(width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #Live Videos
    capture.set(3, width)
    capture.set(4, height)

    #resized_image = rescaleFrame(img)
    #cv.show('Image', resized_image)

#Reading videos
capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
    capture.release()
    cv.destroyAllWindows()
