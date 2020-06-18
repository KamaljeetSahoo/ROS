import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class show_proccessed_output:
    def __init__(self):
        self.sub_img = rospy.Subscriber('processed_img', Image, self.callback)
        self.bridge = CvBridge()

    def callback(self, data):
        cv2_image  = self.bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')
        cv2.imshow('Output_image', cv2_image)
        cv2.waitKey(1)

if __name__ == '__main__':
    rospy.init_node('output_node', anonymous=False)
    b = show_proccessed_output()
    rospy.spin()
