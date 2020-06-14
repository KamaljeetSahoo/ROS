import rospy
from std_msgs.msg import Int64


class squaring_node():
    def __init__(self):
        self.sub = rospy.Subscriber('integers', Int64, self.callback)
        self.pub = rospy.Publisher('squared_integers', Int64, queue_size=10)

    def callback(self, data):
        rospy.loginfo(data.data)
        x = data.data
        self.publishing_squares(x)
        #i = (self.x) * (self.x)
        #self.pub.publish(i)

    def publishing_squares(self, i):
        self.pub.publish(i*i)
        return 0


if __name__ == '__main__':
    obj = squaring_node()
    rospy.init_node('squares', anonymous=False)
    rospy.spin()
