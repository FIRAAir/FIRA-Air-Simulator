#!/usr/bin/env python3
import roslib; roslib.load_manifest('teleop_twist_keyboard')
import rospy

from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

import sys, select, termios, tty

msg = """
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   q    w    e
   a    s    d
   z    x    c

For Holonomic mode (strafing), hold down the shift key:
---------------------------
   U    I    O
   J    K    L
   M    <    >

t : up (+z)
b : down (-z)

anything else : stop

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%

CTRL-C to quit
"""

moveBindings = {
		'w':(1,0,0,0),
		'e':(1,0,0,-1),
		'a':(0,0,0,1),
		'd':(0,0,0,-1),
		'q':(1,0,0,1),
		'x':(-1,0,0,0),
		'c':(-1,0,0,1),
		'z':(-1,0,0,-1),
		'O':(1,-1,0,0),
		'W':(1,0,0,0),
		'E':(0,1,0,0),
		'A':(0,-1,0,0),
		'D':(1,1,0,0),
		'Q':(-1,0,0,0),
		'X':(-1,-1,0,0),
		'C':(-1,1,0,0),
		'i':(0,0,1,0),
		'k':(0,0,-1,0),
	       }

speedBindings={
		'y':(1.1,1.1),
		'h':(.9,.9),
		't':(1.1,1),
		'g':(.9,1),
		'p':(1,1.1),
		';':(1,.9),
	      }

def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key

speed = .5
turn = 1

def vels(speed,turn):
	return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
	settings = termios.tcgetattr(sys.stdin)
	
	pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
	rospy.init_node('teleop_twist_keyboard')
	pub2 = rospy.Publisher('drone/takeoff', Empty, queue_size = 1)
	pub3 = rospy.Publisher('drone/land', Empty, queue_size = 1)
	empty_msg = Empty()

	x = 0
	y = 0
	z = 0
	th = 0
	status = 0

	try:
		print(msg)
		print(vels(speed,turn))
		while(1):
			key = getKey()
			if key in moveBindings.keys():
				x = moveBindings[key][0]
				y = moveBindings[key][1]
				z = moveBindings[key][2]
				th = moveBindings[key][3]
			elif key in speedBindings.keys():
				speed = speed * speedBindings[key][0]
				turn = turn * speedBindings[key][1]

				print(vels(speed,turn))
				if (status == 14):
					print(msg)
				status = (status + 1) % 15
				
			elif key == '1':
			    pub2.publish(empty_msg)
			elif key == '2':
			    pub3.publish(empty_msg)
			
			else:
				x = 0
				y = 0
				z = 0
				th = 0
				if (key == '\x03'):
					break

			twist = Twist()
			twist.linear.x = x*speed; twist.linear.y = y*speed; twist.linear.z = z*speed;
			twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = th*turn
			pub.publish(twist)
			
	except:
		print(e)

	finally:
		twist = Twist()
		twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
		twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
		pub.publish(twist)

		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)


