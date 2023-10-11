#!/user/bin/python3

#########################
# Author: Trenton Foster
# Receive comms from arduino
# Responsible for monitoring arduino for authentication attempts.
#########################

import serial
import time
import sys
import os
from picamera import PiCamera
from datetime import datetime
# Initialize serial communication
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1.0)
time.sleep(1)
ser.reset_input_buffer()
print("Monitoring serial")

# Initialize camera object
cam = PiCamera()

def take_picture(string : str):
    # Filename is determined by date and time
    filepath = "/home/pi/Documents/F2023Capstone/auth_attempts/" + string + "_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
    cam.capture(filepath)

    # Ensure that you aren't using up too much space by artificially limiting your usage to 100 images
    list_of_files = os.listdir('/home/pi/Documents/F2023Capstone/auth_attempts/')
    full_path = ["/home/pi/Documents/F2023Capstone/auth_attempts/{0}".format(x) for x in list_of_files]

    if len(list_of_files) >= 100:
        oldest_file = min(full_path, key=os.path.getctime)
        os.remove(oldest_file)

try:
    # Loop until an authentication is completed
    while True:
        # Sleep momentarily to reduce CPU utilization
        time.sleep(0.01)
        # Check if data is received from arduino
        if ser.in_waiting > 0:
            # read a line from the serial monitor
            line = ser.readline().decode('utf-8')

            # If the MASTER RFID is read
            if "Master access" in line:
                # Take picture of 'postman'
                take_picture("postman")
                print("Postman identified, opening mailbox...")
                ser.close()
                # Exit with status notifying auth.sh of master access
                sys.exit(1)
            
            #if USER RFID is read
            if "User access" in line:
                # Take picture of user
                take_picture("user_RFID_success")
                print("Homeowner identified, please authenticate finger.")
                ser.close()
                # Exit with status notifying auth.sh of user access
                sys.exit(2)
            
            # if unauthenticated RFID is read
            if "Access denied" in line:
                # Take picture of 'thief'
                take_picture("thief_RFID_attempt")
                print("Possible thief detected. Try again")
                # Do not close serial and exit so that user may try another RFID

            # If an authenticated finger is found
            if "Found ID" in line:
                take_picture("authenticated_user")
                # Close comms
                print("Authentication attempt successful! Closing serial")
                ser.close()
                # Exit with successful exit status
                sys.exit(0)
            
            # If an unauthenticated finger is detected
            if "Did not find a match" in line:
                take_picture("unauthenticated_finger_scan")
                print("Authentication attempt failed. Try again")
                # Do not close serial and exit so that user may try another fingerprint scan


except KeyboardInterrupt:
    print ("Serial comm closed")
    ser.close()