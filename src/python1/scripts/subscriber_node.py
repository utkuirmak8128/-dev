#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("RECEİVED DATA: %")

def listener():
    rospy.init_node("Subscriber_Node", anonymous=True)
    rospy.Subscriber("bz2_node", String, callback )
    rospy.spin()
    

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
