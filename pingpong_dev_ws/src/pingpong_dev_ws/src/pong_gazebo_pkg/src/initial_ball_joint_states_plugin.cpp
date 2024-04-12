/**
 * This file creates a plugin for the initial joint state configuation
 * of our ball.
 *
 * This is necessary because the urdf seems to have difficulty with
 * the initial configuration of joint states.
 */

// Header files for Gazebo API
#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo/common/common.hh>
#include <gazebo/physics/PhysicsType.hh>
#include <gazebo/physics/Model.hh>
#include <gazebo/physics/Link.hh>
#include <gazebo/physics/Joint.hh>
#include <gazebo/sdf/sdf.hh>

// Header file for ROS modular find_package functionality
#include <ros/ros.h>

#include <urdf/model.h>
#include <tinyxml.h>

#include <ignition/math/Pose3.hh>
#include <ignition/math/Vector3.hh>

namespace gazebo
{
    class InitialBallJointStatePlugin : public ModelPlugin
    {
    public:
        void Load(physics::ModelPtr _parent, sdf::ElementPtr _sdf)
        {
            // Loads the urdf file
            urdf::Model pong_working_urdf_model;
            if(!pong_working_urdf_model.initFile("$(find pong_gazebo_pkg)/models/pong_working.urdf.xacro")) {
                ROS_ERROR("Failed to parse urdf file");
                return -1;
            }
            ROS_INFO("Successfully parsed urdf file");

            // Get the joint from the URDF file
            std::string joint_name = "table_to_ball_joint";
            urdf::JointConstSharedPtr table_to_ball_joint = pong_working_urdf_model->getJoint(joint_name);

            /**
             * Define the desired position of the ball.
             *
             * In our context, this will mean that the ball
             * will be on top of the table (tentatively*)
             */

            // Defines the desired initial position of the ball (relative to table_link)
            auto initial_ball_position = std::make_tuple(1, 1, 1);
            auto [x, y, z] = initial_ball_position;

            // Sets the position of the ball through the joint
            table_to_ball_joint->SetPosition(0, x, y, z);
        }
    };
    GZ_REGISTER_MODEL_PLUGIN(InitialBallJointStatePlugin)
}

