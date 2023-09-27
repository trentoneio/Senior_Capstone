#!/user/bin/python3

#########################
# Author: Trenton Foster
# Receive comms from arduino
# Responsible for monitoring arduino for a successful finger authentication attempt.
#########################

import serial
import time
import sys

# Initialize serial communication
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1.0)
time.sleep(1)
ser.reset_input_buffer()
print("Monitoring serial")

try:
    # Loop until an authenticated finger is read
    while True:
        # Check if data is received from arduino
        if ser.in_waiting > 0:
            # read a line from the serial monitor
            line = ser.readline().decode('utf-8')
            if "Found ID" in line:
                # Close comms
                print("Authentication attempt successful! Closing serial")
                ser.close()
                # Exit with successful exit status
                sys.exit(0)
            if "Did not find a match" in line:
                # Close comms
                print("Authentication attempt failed. Try again")

except KeyboardInterrupt:
    print ("Serial comm closed")
    ser.close()