#!/bin/bash

# This code provides, frankly, a pretty terrible, but easy wrapper around avrdude.
# Using this script you can upload hex files from a RPi to a arduino. All you need to do is:
# 1. Locate the .hex file to upload (https://www.aranacorp.com/en/generating-and-uploading-hex-files-to-an-arduino/)
# 2. Enter this the location of the on the CLI directly behind the script name when calling this script

UPLOAD_LOC=$1
/home/pi/Downloads/arduino-1.8.19/hardware/tools/avr/bin/avrdude -C/home/pi/Downloads/arduino-1.8.19/hardware/tools/avr/etc/avrdude.conf -v -patmega328p -carduino -P/dev/ttyACM0 -b115200 -D -Uflash:w:$UPLOAD_LOC:i
