
(cl:in-package :asdf)

(defsystem "pingpong-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "BallStateStamped" :depends-on ("_package_BallStateStamped"))
    (:file "_package_BallStateStamped" :depends-on ("_package"))
  ))