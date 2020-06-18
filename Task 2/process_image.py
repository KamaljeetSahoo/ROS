import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class process_image:
    def __init__(self):
        self.sub_img = rospy.Subscriber('input_img', Image, self.callback)
        self.pub_img = rospy.Publisher('processed_img', Image, queue_size=1)
        self.bridge = CvBridge()

    def callback(self, data):
        img_msg = data
        cv2_image = self.bridge.imgmsg_to_cv2(img_msg, desired_encoding='passthrough')
        self.process_img(cv2_image)

    def process_img(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.publish_processed_img(gray)

    def publish_processed_img(self, processed_img):
        processed_img_msg = self.bridge.cv2_to_imgmsg(processed_img, encoding='passthrough')
        self.pub_img.publish(processed_img_msg)

if __name__ == '__main__':
    rospy.init_node('process_img_node', anonymous=False)
    obj=process_image()
    rospy.spin()
