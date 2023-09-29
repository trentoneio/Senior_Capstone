#!/user/bin/python3

# Author: Raspberry Pi @ https://www.youtube.com/watch?v=VzYGDq0D1mw&t=54s
# Take an image using the RPi camera module

from picamera import PiCamera
from time import sleep

# Create camera object
camera = PiCamera()

# Get camera preview window
# alpha is preview window opacity where (0 is fully transparent, 255 no transparency)
camera.start_preview(alpha=192)

# Sleep allows for preview window to be... well usable
sleep (5)

# Capture image after sleep time
camera.capture("/home/pi/Desktop/pic1.jpg")

#Close preview window
camera.stop_preview()
