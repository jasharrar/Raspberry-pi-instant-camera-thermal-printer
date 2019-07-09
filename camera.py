#!/bin/bash
 
SHUTTER=21
LED=5
 
# Initialize GPIO states
gpio -g mode  $SHUTTER up
gpio -g mode  $LED     out
 
 
while :
do
	# Check for shutter button
	if [ $(gpio -g read $SHUTTER) -eq 0 ]; then
		gpio -g write $LED 1
		raspistill -n -t 200 -w 512 -h 384 -o - | lp
 
		sleep 1
		# Wait for user to release button before resuming
		while [ $(gpio -g read $SHUTTER) -eq 0 ]; do continue; done
		gpio -g write $LED 0
	fi
 

done