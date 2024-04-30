import pyrealsense2 as rs
import numpy as np
import cv2 as cv

# Initialize RealSense camera
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
pipeline.start(config)

try:
    while True:
        # Collect both color and depth images/frames from camera
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        if not depth_frame or not color_frame:
            continue

        # Convert color image to numpy array
        color_image = np.asanyarray(color_frame.get_data())

        # Convert color image to HSV
        hsv_image = cv.cvtColor(color_image, cv.COLOR_BGR2HSV)

        # Define lower and upper bounds for orange color in HSV
        lower_orange = np.array([0, 100, 100])
        upper_orange = np.array([20, 255, 255])

        # Threshold the HSV image to get only orange regions
        orange_mask = cv.inRange(hsv_image, lower_orange, upper_orange)

        # Find contours of orange regions
        contours, _ = cv.findContours(orange_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        # Draw contours on the color image
        cv.drawContours(color_image, contours, -1, (0, 255, 0), 2)

        # Detect circles only within orange regions
        for contour in contours:
            # Get bounding box of contour
            x, y, w, h = cv.boundingRect(contour)
            # Extract ROI from color image
            roi_color = color_image[y:y+h, x:x+w]
            # Convert ROI to grayscale
            gray_roi = cv.cvtColor(roi_color, cv.COLOR_BGR2GRAY)
            # Apply blur to reduce noise
            blurred_roi = cv.GaussianBlur(gray_roi, (9, 9), 0)
            # Detect circles using Hough Circle Transform
            circles = cv.HoughCircles(blurred_roi, cv.HOUGH_GRADIENT, dp=1, minDist=50,
                                       param1=50, param2=30, minRadius=10, maxRadius=100)
            # Draw detected circles
            if circles is not None:
                circles = np.round(circles[0, :]).astype("int")
                for (x_circle, y_circle, r_circle) in circles:
                    # Offset circle center coordinates by contour bounding box coordinates
                    x_circle += x
                    y_circle += y
                    # Draw circle on color image
                    cv.circle(color_image, (x_circle, y_circle), r_circle, (0, 255, 0), 4)
                    depth = depth_frame.get_distance(int(x_circle), int(y_circle))  # Get depth (z) value from RealSense depth frame
                    if depth != 0.0:
                        print("Ball coordinates (x, y, z): ", x, y, depth)

        # Display the color image with detected circles
        cv.imshow('Detected Circles', color_image)

        # Break the loop if 'q' is pressed
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Stop streaming
    pipeline.stop()
    cv.destroyAllWindows()
