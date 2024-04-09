import pyrealsense2 as rs
import numpy as np
import cv2

# Initialize RealSense pipeline
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
pipeline.start(config)

# Define color threshold for ball detection
lower_color = np.array([0, 0, 0])  # Lower bound color rgb
upper_color = np.array([255, 255, 255])  # Upper bound rgb

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
        color_mask = cv2.inRange(color_image, lower_color, upper_color)
        blur_ball_frame = cv2.GaussianBlur(color_mask, (11, 11), 0)
        detected_circles = cv2.HoughCircles(blur_ball_frame, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=200, param2=30, minRadius=0, maxRadius=0)
        print(len(detected_circles))
        if detected_circles is not None:
            for circle in detected_circles[0]:
                x, y = circle[:2]  # Extract x, y coordinates of the detected circle
                z = depth_frame.get_distance(int(x), int(y))  # Get depth (z) value from RealSense depth frame
                print("Ball coordinates (x, y, z):", x, y, z)

        # Display the frames with detected circles
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', color_image)
        cv2.waitKey(1)

finally:
    # Stop streaming
    pipeline.stop()