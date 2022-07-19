#!/usr/bin/env python3 
import rospy 
import rospkg 
from gazebo_msgs.msg import ModelState 
from gazebo_msgs.srv import SetModelState
from gazebo_msgs.srv import GetModelState
from random import randint 

def main():
    rospy.init_node('set_pose')
    rospy.wait_for_service('/gazebo/get_model_state')
    # rospy.Rate(5)
    model = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    rand_x = -1 + (randint(-1, 1))
    # while not rospy.is_shutdown():
    if(model('gate_system', 'gate_system')):
        state_msg = ModelState()
        state_msg.model_name = 'gate_system'
        state_msg.pose.position.x = rand_x
        state_msg.pose.position.y = -4
        state_msg.pose.position.z = 0
        # state_msg.pose.orientation.x = 0
        # state_msg.pose.orientation.y = 0
        # state_msg.pose.orientation.z = 3.14
        # state_msg.pose.orientation.w = 0
        
        rospy.wait_for_service('/gazebo/set_model_state')
        try:
            set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
            resp = set_state( state_msg )
            rospy.loginfo("Moved the gate")

        except rospy.ServiceException:
            print("err") 
                                        

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass