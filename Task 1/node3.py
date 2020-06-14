import rospy
from std_msgs.msg import Int64

class node3():
    def __init__(self):
        self.sub = rospy.Subscriber('squared_integers', Int64, self.callback)

    def callback(self, data):
        #rospy.loginfo(data.data)
        print(data.data)



if __name__ == '__main__':
    obj = node3()
    rospy.init_node('printing_node', anonymous=False)
    obj = node3()
    rospy.spin()
