// Generated by gencpp from file pingpong/BallStateStamped.msg
// DO NOT EDIT!


#ifndef PINGPONG_MESSAGE_BALLSTATESTAMPED_H
#define PINGPONG_MESSAGE_BALLSTATESTAMPED_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <geometry_msgs/Point.h>
#include <geometry_msgs/Vector3.h>
#include <geometry_msgs/Vector3.h>

namespace pingpong
{
template <class ContainerAllocator>
struct BallStateStamped_
{
  typedef BallStateStamped_<ContainerAllocator> Type;

  BallStateStamped_()
    : Header()
    , position()
    , velocity()
    , angular_velocity()  {
    }
  BallStateStamped_(const ContainerAllocator& _alloc)
    : Header(_alloc)
    , position(_alloc)
    , velocity(_alloc)
    , angular_velocity(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _Header_type;
  _Header_type Header;

   typedef  ::geometry_msgs::Point_<ContainerAllocator>  _position_type;
  _position_type position;

   typedef  ::geometry_msgs::Vector3_<ContainerAllocator>  _velocity_type;
  _velocity_type velocity;

   typedef  ::geometry_msgs::Vector3_<ContainerAllocator>  _angular_velocity_type;
  _angular_velocity_type angular_velocity;





  typedef boost::shared_ptr< ::pingpong::BallStateStamped_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pingpong::BallStateStamped_<ContainerAllocator> const> ConstPtr;

}; // struct BallStateStamped_

typedef ::pingpong::BallStateStamped_<std::allocator<void> > BallStateStamped;

typedef boost::shared_ptr< ::pingpong::BallStateStamped > BallStateStampedPtr;
typedef boost::shared_ptr< ::pingpong::BallStateStamped const> BallStateStampedConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pingpong::BallStateStamped_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pingpong::BallStateStamped_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::pingpong::BallStateStamped_<ContainerAllocator1> & lhs, const ::pingpong::BallStateStamped_<ContainerAllocator2> & rhs)
{
  return lhs.Header == rhs.Header &&
    lhs.position == rhs.position &&
    lhs.velocity == rhs.velocity &&
    lhs.angular_velocity == rhs.angular_velocity;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::pingpong::BallStateStamped_<ContainerAllocator1> & lhs, const ::pingpong::BallStateStamped_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace pingpong

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::pingpong::BallStateStamped_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pingpong::BallStateStamped_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pingpong::BallStateStamped_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pingpong::BallStateStamped_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pingpong::BallStateStamped_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pingpong::BallStateStamped_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pingpong::BallStateStamped_<ContainerAllocator> >
{
  static const char* value()
  {
    return "256ca3a068a64b87055779e0d461b484";
  }

  static const char* value(const ::pingpong::BallStateStamped_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x256ca3a068a64b87ULL;
  static const uint64_t static_value2 = 0x055779e0d461b484ULL;
};

template<class ContainerAllocator>
struct DataType< ::pingpong::BallStateStamped_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pingpong/BallStateStamped";
  }

  static const char* value(const ::pingpong::BallStateStamped_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pingpong::BallStateStamped_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header Header\n"
"geometry_msgs/Point position\n"
"geometry_msgs/Vector3 velocity\n"
"geometry_msgs/Vector3 angular_velocity\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Vector3\n"
"# This represents a vector in free space. \n"
"# It is only meant to represent a direction. Therefore, it does not\n"
"# make sense to apply a translation to it (e.g., when applying a \n"
"# generic rigid transformation to a Vector3, tf2 will only apply the\n"
"# rotation). If you want your data to be translatable too, use the\n"
"# geometry_msgs/Point message instead.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
;
  }

  static const char* value(const ::pingpong::BallStateStamped_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pingpong::BallStateStamped_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.Header);
      stream.next(m.position);
      stream.next(m.velocity);
      stream.next(m.angular_velocity);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct BallStateStamped_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pingpong::BallStateStamped_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pingpong::BallStateStamped_<ContainerAllocator>& v)
  {
    s << indent << "Header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.Header);
    s << indent << "position: ";
    s << std::endl;
    Printer< ::geometry_msgs::Point_<ContainerAllocator> >::stream(s, indent + "  ", v.position);
    s << indent << "velocity: ";
    s << std::endl;
    Printer< ::geometry_msgs::Vector3_<ContainerAllocator> >::stream(s, indent + "  ", v.velocity);
    s << indent << "angular_velocity: ";
    s << std::endl;
    Printer< ::geometry_msgs::Vector3_<ContainerAllocator> >::stream(s, indent + "  ", v.angular_velocity);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PINGPONG_MESSAGE_BALLSTATESTAMPED_H
