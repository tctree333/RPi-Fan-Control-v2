#!/bin/bash
PIN=18
ARG=$1
TEMP=$(/opt/vc/bin/vcgencmd measure_temp)
echo $TEMP

if [ ! -d /sys/class/gpio/gpio$PIN ]; then
# Sets pin $PIN as an output
echo $PIN > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio$PIN/direction
STATE=$(sudo cat /sys/class/gpio/gpio$PIN/value)
fi

if [[ $ARG == "on" ]]
then
echo "1" > /sys/class/gpio/gpio$PIN/value
echo Fan Turned On
elif [[ $ARG == "off" ]]
then
echo "0" > /sys/class/gpio/gpio$PIN/value
echo Fan Turned Off
elif [[ $ARG == "" ]]
then
STATE=$(sudo cat /sys/class/gpio/gpio$PIN/value)
    if [[ $STATE == 1 ]]
    then
    echo Fan Is On
    elif [[ $STATE == 0 ]]
    then
    echo Fan Is Off
    else
    echo Error, Please Try Again
    fi
else
echo Invalid Argument $ARG
fi

STATE=$(sudo cat /sys/class/gpio/gpio$PIN/value)
if [[ $STATE == 0 ]]
then
echo "$PIN" > /sys/class/gpio/unexport
fi
