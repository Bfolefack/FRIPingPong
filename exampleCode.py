import pyrealsense2 as rs
import numpy as np
import cv2 as cv

#Create orange arrays (Constant)
lower_pink = np.array([5, 50, 50])
upper_pink = np.array([15, 255, 255])


# Initialize RealSense camera 
pipeline = rs.pipeline()
config = rs.config()

# Standby code if needed to switch to lower resolution 
#config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
#config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Enable color and depth stream with resolution of 1280x720
config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
pipeline.start(config)


try:
    while True:
        #Collect both color and depth images/frames from camera
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        if not depth_frame or not color_frame:
            continue

        # Convert color image to numpy array
        color_image = np.asanyarray(color_frame.get_data())


        # Applies color masking to identify only the ball
        pink_mask = cv.inRange(color_image, lower_pink, upper_pink)
        blur_ball_frame = cv.GaussianBlur(pink_mask, (11, 11), 0)
        ballContours = cv.findContours(pink_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        

        if len(ballContours[0]) != 0 : #Software still runs even if ball is not detected
            x, y, w, h = cv.boundingRect(ballContours[0][0]) #Collect dimensions of bounding rectangle 
            cv.rectangle(color_image, (x, y), (x + w, y + h), (0, 255, 0), 2) #Draw rectangle around ball
            x_center = x + (w/2) #Calculate coordinates of the ball's center 
            y_center = y + (h/2)
            depth = depth_frame.get_distance(int(x_center), int(y_center))  # Get depth (z) value depth frame
            if depth != 0.0: #Remove Noise
                print("Ball coordinates (x, y, z): ", x, y, depth) #Prints ball coordinates in terminal 
                """
                Prints BGR values of detected ball
                frameWidth = color_frame.get_width()
                colorIndex = y * frameWidth + x
                colorBGR = color_frame.get_data()[colorIndex * 3 : colorIndex * 3 + 3]
                print("BGR: ", colorBGR)
                """
                cv.putText(color_image, f'X: {x_center}, Y: {y_center}, Z: {depth:.2f}', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2) #Print ball coordinates on camera window 
        else: 
            print("No ball detected") #Ball not found 
            
            
        # Display the frames with detected circles
        cv.namedWindow('RealSense', cv.WINDOW_AUTOSIZE)
        cv.imshow('RealSense', color_image)
        if cv.waitKey(1) & 0xFF == ord('x'): #Press x to kill 
            break

finally:
    # Stop streaming
    pipeline.stop()