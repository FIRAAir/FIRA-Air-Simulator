# FIRA-Air-Simulator
FIRA Air Simulator

## Changelog
### Update 1.0.2
- Fixed rotating_link motion (Changed to Constant speed)
- Fixed the slight movement of gate on the scene
- Removed the "H" tag next to the gate
- Fixed launch errors and robot spawn errors (Please make sure to run ```rosrun fira_challenge_env model_update.py```)
- Added bash file "run.sh" to run the simulator
- Added Model updater to fix the static paths in the world files
- Updated gate physical parameters

### Tested Minimum Local Hardware Requirements
CPU: Intel® Core™ i5-5257U CPU @ 2.70GHz <br/>
GPU: Intel® Iris 6100 <br/>
RAM: 8 GB

### Software Requirements
Ubuntu 20.04 and ROS Noetic used exclusively. Other versions are not officially supported.
Prior to installing our software make sure to have ROS and Catkin tools installed: http://wiki.ros.org/noetic/Installation/Ubuntu
```bash
sudo apt install python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
sudo apt-get install python3-catkin-tools
sudo apt install python3-wstool
sudo apt install ros-noetic-ros-control
pip3 install catkin_pkg
```

### Installation
```bash
# Setup catkin workspace
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin init
# Add workspace to bashrc.
echo 'source ~/catkin_ws/devel/setup.bash' >> ~/.bashrc
cd src
git clone https://github.com/Amxrmohammad/FIRA-Air-Simulator.git
cd ..
catkin_make
source ~/.bashrc

# Make sure to run the following line to update static paths (Important) 
rosrun fira_challenge_env model_update.py
```
The installation process is done.

### Usage (Updated)
```bash
roscd fira_challenge_env
cd script
./run.sh
```
The drone can be controlled through the /cmd_vel topic using a Twist type message. teleop_keyboard_twist can also be used to controll the drone using keyboard.
