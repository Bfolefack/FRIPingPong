; Auto-generated. Do not edit!


(cl:in-package pingpong_dev_ws-msg)


;//! \htmlinclude BallStateStamped.msg.html

(cl:defclass <BallStateStamped> (roslisp-msg-protocol:ros-message)
  ((Header
    :reader Header
    :initarg :Header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (position
    :reader position
    :initarg :position
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (velocity
    :reader velocity
    :initarg :velocity
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (angular_velocity
    :reader angular_velocity
    :initarg :angular_velocity
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3)))
)

(cl:defclass BallStateStamped (<BallStateStamped>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BallStateStamped>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BallStateStamped)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pingpong_dev_ws-msg:<BallStateStamped> is deprecated: use pingpong_dev_ws-msg:BallStateStamped instead.")))

(cl:ensure-generic-function 'Header-val :lambda-list '(m))
(cl:defmethod Header-val ((m <BallStateStamped>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pingpong_dev_ws-msg:Header-val is deprecated.  Use pingpong_dev_ws-msg:Header instead.")
  (Header m))

(cl:ensure-generic-function 'position-val :lambda-list '(m))
(cl:defmethod position-val ((m <BallStateStamped>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pingpong_dev_ws-msg:position-val is deprecated.  Use pingpong_dev_ws-msg:position instead.")
  (position m))

(cl:ensure-generic-function 'velocity-val :lambda-list '(m))
(cl:defmethod velocity-val ((m <BallStateStamped>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pingpong_dev_ws-msg:velocity-val is deprecated.  Use pingpong_dev_ws-msg:velocity instead.")
  (velocity m))

(cl:ensure-generic-function 'angular_velocity-val :lambda-list '(m))
(cl:defmethod angular_velocity-val ((m <BallStateStamped>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pingpong_dev_ws-msg:angular_velocity-val is deprecated.  Use pingpong_dev_ws-msg:angular_velocity instead.")
  (angular_velocity m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BallStateStamped>) ostream)
  "Serializes a message object of type '<BallStateStamped>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'Header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'position) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'velocity) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'angular_velocity) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BallStateStamped>) istream)
  "Deserializes a message object of type '<BallStateStamped>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'Header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'position) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'velocity) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'angular_velocity) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BallStateStamped>)))
  "Returns string type for a message object of type '<BallStateStamped>"
  "pingpong_dev_ws/BallStateStamped")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BallStateStamped)))
  "Returns string type for a message object of type 'BallStateStamped"
  "pingpong_dev_ws/BallStateStamped")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BallStateStamped>)))
  "Returns md5sum for a message object of type '<BallStateStamped>"
  "256ca3a068a64b87055779e0d461b484")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BallStateStamped)))
  "Returns md5sum for a message object of type 'BallStateStamped"
  "256ca3a068a64b87055779e0d461b484")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BallStateStamped>)))
  "Returns full string definition for message of type '<BallStateStamped>"
  (cl:format cl:nil "Header Header~%geometry_msgs/Point position~%geometry_msgs/Vector3 velocity~%geometry_msgs/Vector3 angular_velocity~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BallStateStamped)))
  "Returns full string definition for message of type 'BallStateStamped"
  (cl:format cl:nil "Header Header~%geometry_msgs/Point position~%geometry_msgs/Vector3 velocity~%geometry_msgs/Vector3 angular_velocity~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BallStateStamped>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'Header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'position))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'velocity))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'angular_velocity))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BallStateStamped>))
  "Converts a ROS message object to a list"
  (cl:list 'BallStateStamped
    (cl:cons ':Header (Header msg))
    (cl:cons ':position (position msg))
    (cl:cons ':velocity (velocity msg))
    (cl:cons ':angular_velocity (angular_velocity msg))
))
