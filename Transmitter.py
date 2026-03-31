import time
import serial

lora = serial.Serial(port='/dev/ttyS0',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)

count = 0

print("Starting transmission")

message = "Hello Baja2"
UPDATE = 50     # Update log every 10 seconds
DELAY = 0.2     # Transmit every 200ms

while True:
    if count % UPDATE == 0:
        print(f"{message} broadcast for {count*DELAY} seconds")
    
    b = bytes(message,'utf-8')#convert string into bytes
    s = lora.write(b)#send the data to other lora
    count += 1
    time.sleep(DELAY)

