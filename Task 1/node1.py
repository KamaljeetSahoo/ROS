import rospy
from std_msgs.msg import Int64

def node1():
    pub = rospy.Publisher('integers', Int64, queue_size=10)
    rospy.init_node('int_publish', anonymous=False)
    rate = rospy.Rate(10)
    i = 0
    while not rospy.is_shutdown():
            rospy.loginfo(i)
            pub.publish(i)
            rate.sleep()
            i+=1


if __name__ == '__main__':
    try:
        node1()
    except rospy.ROSInterruptException:
        pass
