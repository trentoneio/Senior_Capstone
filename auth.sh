#!/bin/bash

#########################
# Author: Trenton Foster
# Authentication driver
# Responsible for the complete process of authenticating a finger on the fingerprint scanner.
#########################

# Upload fingerprint reading script to arduino
./upload_to_arduino.sh /home/pi/Documents/F2023Capstone/Build/fingerprint/fingerprint.ino.hex
# Start python module to read output from arduino
python3 finger_auth.py
# Upload an empty file to the arduino to turn off fingerprint scanner and conserve power
./upload_to_arduino.sh /home/pi/Documents/F2023Capstone/Build/nothing/nothing.ino.hex

