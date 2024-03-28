
import cv2 as cv 
import numpy as np

#class Ball_Detection:

    #def is_ppball(image_path):
        
ballVideoStream = cv.VideoCapture(0)

while True:
    ret, ballFrame = ballVideoStream.read()
    if not ret: break


    greyBallFrame = cv.cvtColor(ballFrame, cv.COLOR_BGR2GRAY)
    blurBallFrame = cv.GaussianBlur(greyBallFrame, (9,9), 0) #Reduce Noise

    detectedShape = cv.HoughCircles(blurBallFrame, cv.HOUGH_GRADIENT, dp=1, minDist=50, param1=200, param2=30, minRadius=0, maxRadius=0)

    if detectedShape is not None:
        detectedShape = np.round(detectedShape[0, :]).astype("int")
        for (x, y, r) in detectedShape:
            cv.circle(ballVideoStream, (x, y), r, (0, 255, 0), 2)


    cv.imshow("ball frame", ballVideoStream)
    if cv.waitKey(1) & 0xFF == ord('x'): break #Press x to close out webcam window 

ballVideoStream.release()
cv.destroyAllWindows


