## My Setup

### Hardware
* Raspberry Pi
* DIYmall Optical Fingerprint Reader Sensor Module (https://www.amazon.com/Optical-Fingerprint-Reader-Arduino-Mega2560/dp/B077GKPWMN)

### Software
* Adafruit Fingerprint Sensor Library (https://github.com/adafruit/Adafruit-Fingerprint-Sensor-Library)

## What I Learned
After a bit of testing with the "enroll" and "fingerpint" projects included in the Adafruit Fingerprint Sensor Library for Arduino, I learend these things:
1. Fingerprints may be scanned and saved using the "enroll" project. I may or may not have to modify this. For now (09/25), it will be towards the bottom of my to do list as the scope of our mailbox project does not revlolve around 'user setup'. However, this could be something for me to come back to later. All fingerprints that are scanned are stored to the Arduino's onboard flash memory. A limit of 127 fingerprints may be stored
2. Fingerprints may be scanned and checked against saved scanns using the "fingerint" project. I WILL have to modify this a bit so that the RPi is alerted of a successful scan or an unsuccessful scan. However, I will not need to alter the core logic of this program.

For now, these are the only two things that I see myself needing to use or alter. However, that could possibly change.