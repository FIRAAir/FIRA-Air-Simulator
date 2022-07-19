#!/usr/bin/env python3
import rospy 
import rospkg 
import os


def main():
    rospy.init_node('start_spin')

    os.system("rosservice call --wait /gazebo/apply_body_wrench '{body_name: rotating_link , wrench: { force: { x: 0, y: 0 , z: -11 } }, start_time: 0, duration: 1000000000 }'")



if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass