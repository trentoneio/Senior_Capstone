#!/bin/bash

#########################
# Author: Trenton Foster
# Authentication driver
# Responsible for the complete process of authenticating a finger on the fingerprint scanner.
#########################

function open_mailbox(){
    ./upload_to_arduino.sh /private/tmp/sshfs/home/pi/Documents/F2023Capstone/Build/open_solenoid/open_solenoid.ino.hex
    echo "Mailbox unlocked for 30s"
    sleep 35
    echo "Mailbox locked"
}

#Upload RFID reading script to arduino
./upload_to_arduino.sh /home/pi/Documents/F2023Capstone/Build/RFID/RFID.ino.hex
# Start python module to read output from arduino
python3 auth.py
AUTH_EXIT_STATUS=$?

case $AUTH_EXIT_STATUS in
    # If postman prensents RFID
    "1")
        # Upload script that opens mailbox
        open_mailbox
        ;;

    # If authentiacated RFID is presented
    "2")
        # Upload fingerprint reading script to arduino
        ./upload_to_arduino.sh /home/pi/Documents/F2023Capstone/Build/fingerprint/fingerprint.ino.hex
        # Start python module to read output from arduino
        python3 auth.py
        AUTH_EXIT_STATUS=$?
        ;;
esac

# If a user is authenticated, open the mailbox
if [[ "$AUTH_EXIT_STATUS" == "0" ]]; then
    open_mailbox
fi

# continuously run this script
./auth.sh
