import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class generate_image:
    def __init__(self):
        self.pub_img = rospy.Publisher('input_img', Image, queue_size=1)
        self.bridge = CvBridge()
        self.cap = cv2.VideoCapture(0)
        self.take_input()

    def take_input(self):
        while not rospy.is_shutdown():
            ret, frame = self.cap.read()
            self.publish_img(frame)
            cv2.imshow('input', frame)
            cv2.waitKey(1)

        self.cap.release()

    def publish_img(self, cv2_image):
        image_message = self.bridge.cv2_to_imgmsg(cv2_image, encoding="passthrough")
        self.pub_img.publish(image_message)


if __name__ == '__main__':
    rospy.init_node('Camera', anonymous=False)
    x = generate_image()

    try:
        rospy.spin()
    except Keyboardinterrupt:
        print("Shutting Down")
    cv2.destroyAllWindows()
