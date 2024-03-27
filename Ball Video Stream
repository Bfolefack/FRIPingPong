import cv2 as cv 
import numpy as np

#class Ball_Detection:

    #def is_ppball(image_path):
        
ballVideoStream = cv.VideoCapture(0)

while True:
    ret, ballFrame = ballVideoStream.read()
    if not ret: break

    cv.imshow("ball frame", ballFrame)
    if cv.waitKey(1) & 0xFF == ord('x'): break #Press x to close out webcam window 

ballVideoStream.release()
cv.destroyAllWindows


