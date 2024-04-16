import pyrealsense2 as rs
import numpy as np
import cv2 as cv

#Create orange arrays (Constant)
lower_pink = np.array([0, 70, 70])
upper_pink = np.array([20, 255, 255])


# Initialize RealSense pipeline
pipeline = rs.pipeline()
config = rs.config()
#config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
#config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
pipeline.start(config)


try:
    while True:
        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        if not depth_frame or not color_frame:
            continue

        # Convert color image to numpy array
        color_image = np.asanyarray(color_frame.get_data())


        # Apply color thresholding to detect the ball
        pink_mask = cv.inRange(color_image, lower_pink, upper_pink)
        blur_ball_frame = cv.GaussianBlur(pink_mask, (11, 11), 0)
        ballContours = cv.findContours(pink_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        if ballContours is not None and ballContours[0] is not None:
            #print("ball countours: ",ballContours)
            contourArea = cv.contourArea(ballContours[0][0], False)
            #print("ball area: ",contourArea)
            #if contourArea > 100:
            x, y, w, h = cv.boundingRect(ballContours[0][0])
            cv.rectangle(color_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            xDepth = x + (w/2)
            yDepth = y + (h/2)
            z = depth_frame.get_distance(int(xDepth), int(yDepth))  # Get depth (z) value from RealSense depth frame
            print("Ball coordinates (x, y, z): ", x, y, z)
        else: 
            print("No contours detected")
        # Display the frames with detected circles
        cv.namedWindow('RealSense', cv.WINDOW_AUTOSIZE)
        cv.imshow('RealSense', color_image)
        if cv.waitKey(1) & 0xFF == ord('x'):
            break

finally:
    # Stop streaming
    pipeline.stop()