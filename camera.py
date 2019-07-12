#!/bin/bash

SHUTTER=16
LED=21
LED2=20
LEDSYS=26
SHUTDOWN=19

# Initialize GPIO states
gpio -g mode $SHUTTER up
gpio -g mode $LED     out
gpio -g mode $LED2 out
gpio -g mode $LEDSYS out
gpio -g mode $SHUTDOWN up

# Flash SYSTEM LED on startup (on off on)
for i in `seq 1 5`;
do
        gpio -g write $LEDSYS 1
        sleep 0.2
        gpio -g write $LEDSYS 0
        sleep 0.2
        gpio -g write $LEDSYS 1
done

while :
do
        # Shutter button
        if [ $(gpio -g read $SHUTTER) -eq 0 ]; then
                gpio -g write $LED 1
                gpio -g write $LED2 1
                sleep 0.2
                gpio -g write $LED 0
                gpio -g write $LED2 0
                raspistill -n -t 200 -w 512 -h 384 -o - | lp

                sleep 1
                # Wait for button
                while [ $(gpio -g read $SHUTTER) -eq 0 ]; do continue; done
                gpio -g write $LED 0
                gpio -g write $LED2 0
        fi

        # Shutdown button script
        if [ $(gpio -g read $SHUTDOWN) -eq 0 ]; then
                # hold for 2 seconds
                starttime=$(date +%s)
                while [ $(gpio -g read $SHUTDOWN) -eq 0 ]; do
                        if [ $(($(date +%s)-starttime)) -ge 2 ]; then
                                shutdown -h now
                        fi
                done
        fi

done

