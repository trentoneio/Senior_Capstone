#!/user/bin/python3

import serial
import time

# Initialize serial communcation
ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1.0)
time.sleep(3)
ser.reset_input_buffer()
print("Serial OK")
#ser.close()

#how to recieve comms from arduino
'''
try:
    while True:
        if ser.in_waiting > 0:
            # read a line from the buffer
            line = ser.readline().decode('utf-8')
            print(line)
'''

#how to send comms to arduino
'''
try:
    while True:
        ser.write("Hello from RPi\n".encode('utf-8'))
'''
        
# how to do bidirectional communication
'''
try:
    while True:
        time.sleep(1)
        print("Send message to Arudino")
        ser.write("Hello from RPi\n".encode('utf-8'))
        while ser.in_waiting <=0 :
            time.sleep(0.01)
        response = ser.readline().decode('utf-8')
        print(response)
'''

except KeyboardInterrupt:
    print ("Serial comm closed")
    ser.close()