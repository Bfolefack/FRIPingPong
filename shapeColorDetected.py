import cv2 as cv
import numpy as np
import pyrealsense2 as rs


def get_ball_image_position(self, image: Image):
    return (0.5, 0.5)

def get_ball_position(self):
    #returns x, y, and z coordinates of ball

    # WE NEED TO MOVE ALL OF THE REAL SENSE CONFIG CODE OUTSIDE OF THE METHOD
    ballPipeline = rs.pipeline()
    ballConfig = rs.config()
    ballConfig.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 60) 
    ballConfig.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 60) 
    #^^  Need to review desired resolution, do we want more accuracy or speed?

    try:
         while True:
              ballFrames = ballPipeline.wait_for_frames()
              ballDepthFrame = ballFrames.get_depth_frame()
              ballColorFrame = ballFrames.get_color_frame()
              # ^^ Gets depth frame from RealSense camera

              if not ballDepthFrame:
                   continue
              
              ballColorImage = np.asanyarray(ballColorFrame.get_data()) # Convert to a format OpenCV can understand
              
              ballCenter = image_callback(ballColorImage)

              if ballCenter is not None:
                   ballDepthValue = ballDepthFrame.get_distance(ballCenter[0], ballCenter[1])

                   ballDistance = ballDepthValue / 1000 #Unsure about the dividing by 1000

                   ballCoordinates = np.array(ballCenter[0], ballCenter[1], ballDistance)
                   return ballCoordinates
    finally:
        pass

    #return self.ball_position

def image_callback(msg: Image):
        bridge = CvBridge()
        lower_color = np.array([0, 100, 100])  # Lower bound color rgb
        upper_color = np.array([10, 255, 255])  # Upper bound rgb
        
        # Convert the ROS Image message to OpenCV format
        ballFrameCV = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")

        # Threshold the frame to get only the desired color
        color_mask = cv.inRange(ballFrameCV, lower_color, upper_color)

        # Apply Gaussian blur to reduce noise
        blurBallFrame = cv.GaussianBlur(color_mask, (11, 11), 0)

        # Detect circles in the blurred color-masked frame
        detectedCircles = cv.HoughCircles(blurBallFrame, cv.HOUGH_GRADIENT, dp=1, minDist=50, param1=200, param2=30, minRadius=0, maxRadius=0)
        
        if detectedCircles is not None:
            if len(detectedCircles) == 1:
                #x, y, r = detectedCircles[0][0]
                 x, y = detectedCircles[0][:2]
                #x, y, r is the x, y coordinates with r radius
                #prob will return this
            else:
                print("More than one circle detected.")
        else:
            print("No circle detected.")
        pass