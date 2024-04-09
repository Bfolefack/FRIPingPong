import cv2 as cv 
import numpy as np
import pyrealsense2 as rs


#Create pink arrays (Constant)
lower_pink = np.array([140, 50, 50])
upper_pink = np.array([180, 255, 255])

#Open the video stream
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
pipeline.start(config)


while True:
    frames = pipeline.wait_for_frames()
    # Read a frame from the video stream
    color_frame = frames.get_color_frame()
    if not color_frame: 
        break

    color_image = np.asanyarray(color_frame.get_data())
    # Convert the frame to grayscale
    greyBallFrame = cv.cvtColor(color_image, cv.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurBallFrame = cv.GaussianBlur(greyBallFrame, (11, 11), 0)

    #Apply Pink Mask so only pink things sho up 
    pinkMask = cv.inRange(blurBallFrame, lower_pink, upper_pink)

    # Detect circles in the blurred grayscale frame
    #detectedCircles = cv.HoughCircles(blurBallFrame, cv.HOUGH_GRADIENT, dp=1, minDist=50, param1=200, param2=30, minRadius=0, maxRadius=0)

    # Detect a blob contour using the pink mask 
    ballContours = cv.findContours(pinkMask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Draw circles on the original frame if circles are detected
    """""
    if detectedCircles is not None:
        detectedCircles = np.round(detectedCircles[0, :]).astype("int")
        for (x, y, r) in detectedCircles:
            cv.circle(color_image, (x, y), r, (0, 255, 0), 2)
            print(x, y)
    """

    if ballContours is not None:
        contourArea = cv.contourArea(ballContours)

        if contourArea > 100:
            x, y, w, h = cv.boundingRect(ballContours)
            cv.rectangle(color_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Need to add code to return center of blob


    # Display the frame with detected circles
    cv.imshow("Ball Frame", color_image)

    # Check for the 'x' key press to exit the loop
    if cv.waitKey(1) & 0xFF == ord('x'): 
        break

#Release the video stream and close all OpenCV windows
color_frame.release()
cv.destroyAllWindows()
#something