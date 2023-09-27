#!/bin/bash

#########################
# Author: Trenton Foster
# AVRDUDE wrapper
# Upload a hex file to the arduino using the avrdude tool.
# Arguments:
#  1. The host location of the hex file to upload.
#########################

UPLOAD_LOC=$1
/home/pi/Downloads/arduino-1.8.19/hardware/tools/avr/bin/avrdude \
-C/home/pi/Downloads/arduino-1.8.19/hardware/tools/avr/etc/avrdude.conf \
-v -patmega328p -carduino -P/dev/ttyACM0 -b115200 -D -Uflash:w:$UPLOAD_LOC:i
