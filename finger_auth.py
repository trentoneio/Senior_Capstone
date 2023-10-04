#!/user/bin/python3

#########################
# Author: Trenton Foster
# Receive comms from arduino
# Responsible for monitoring arduino for a successful finger authentication attempt.
#########################

import serial
import time
import sys
from picamera import PiCamera
from datetime import datetime
# Initialize serial communication
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1.0)
time.sleep(1)
ser.reset_input_buffer()
print("Monitoring serial")

# Initialize camera object
cam = PiCamera()

def take_picture(status):
    # Filename is determined by date and time
    filepath = "/home/pi/Documents/F2023Capstone/auth_attempts/" + status + "_" + datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + ".jpg"
    cam.capture(filepath)

try:
    # Loop until an authenticated finger is read
    while True:
        # Sleep momentarily to reduce CPU utilization
        time.sleep(0.01)
        # Check if data is received from arduino
        if ser.in_waiting > 0:
            # read a line from the serial monitor
            line = ser.readline().decode('utf-8')

            # If an authenticated finger is found
            if "Found ID" in line:
                take_picture("success")
                # Close comms
                print("Authentication attempt successful! Closing serial")
                ser.close()
                # Exit with successful exit status
                sys.exit(0)
            
            # If an unauthenticated finger is detected
            if "Did not find a match" in line:
                take_picture("fail")
                print("Authentication attempt failed. Try again")

except KeyboardInterrupt:
    print ("Serial comm closed")
    ser.close()