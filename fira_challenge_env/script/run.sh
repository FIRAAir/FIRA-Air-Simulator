#!/bin/sh
killall -9 rosmaster
killall -9 roslaunch
killall -9 rosout
killall -9 gzserver
killall -9 gzclient
roslaunch fira_challenge_env main.launch