#!/bin/sh
killall -9 rosmaster
killall -9 roslaunch
killall -9 rosout
killall -9 gzserver
killall -9 gzclient
#!/bin/sh

#find where the 'sjtu_drone' is
pack_path=$(rospack find sjtu_drone)

#export the gazebo pathes
export GAZEBO_MODEL_PATH=$pack_path/models:$GAZEBO_MODEL_PATH
export GAZEBO_RESOURCE_PATH=$pack_path:/usr/share/gazebo-11:/usr/share/gazebo-11:/usr/share/gazebo_models:$GAZEBO_RESOURCE_PATH
export GAZEBO_PLUGIN_PATH=$pack_path/plugins:$GAZEBO_PLUGIN_PATH

#call the client of Gazebo
roslaunch fira_challenge_env main.launch 