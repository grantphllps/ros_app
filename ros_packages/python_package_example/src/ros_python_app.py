#!/usr/bin/python3

import rospy

if __name__ == "__main__":
    
    rospy.init_node('talker', anonymous=True)
    
    rospy.loginfo("HELLO FROM MY PYTHON NODE")