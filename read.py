import cv2 as cv

#capturing images
# img =cv.imread('photos/cat.jpg') 

# cv.imshow('Cat', img)

#capturing videos

#capture = cv.VideoCapture(0) #capturing facecam
capture = cv.VideoCapture('videos/Presentation asset.mp4') #capturing a saved video

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
