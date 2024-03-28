import cv2 as cv 
import numpy as np

# Open the video stream
ballVideoStream = cv.VideoCapture(0)


while True:
    # Read a frame from the video stream
    ret, ballFrame = ballVideoStream.read()
    if not ret: 
        break

    # Convert the frame to grayscale
    greyBallFrame = cv.cvtColor(ballFrame, cv.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurBallFrame = cv.GaussianBlur(greyBallFrame, (11, 11), 0)

    # Detect circles in the blurred grayscale frame
    detectedCircles = cv.HoughCircles(blurBallFrame, cv.HOUGH_GRADIENT, dp=1, minDist=50, param1=200, param2=30, minRadius=0, maxRadius=0)

    # Draw circles on the original frame if circles are detected
    if detectedCircles is not None:
        detectedCircles = np.round(detectedCircles[0, :]).astype("int")
        for (x, y, r) in detectedCircles:
            cv.circle(ballFrame, (x, y), r, (0, 255, 0), 2)

    # Display the frame with detected circles
    cv.imshow("Ball Frame", ballFrame)
    
    # Check for the 'x' key press to exit the loop
    if cv.waitKey(1) & 0xFF == ord('x'): 
        break

# Release the video stream and close all OpenCV windows
ballVideoStream.release()
cv.destroyAllWindows()
