# test code for serial port


import serial
import time
lora = serial.Serial('/dev/ttyS0', 9600, timeout=1)
while True:
    lora.write(b"TESTING LORA\n")
    print("Sent: TESTING LORA")
    time.sleep(1)

