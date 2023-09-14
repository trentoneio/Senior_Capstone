import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(3)
ser.reset_input_buffer()
print("Serial OK")
ser.close()