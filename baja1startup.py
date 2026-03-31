import serial
import time

port = '/dev/ttyS0'
ser = serial.Serial(port, 9600, timeout=1)

def log_to_file(data):
    with open("connection_log.txt", "a") as f:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{timestamp}] {data}\n")
    print(data) # Still print to screen so you can see it

log_to_file("--- MASTER START: PING MODE ---")

try:
    while True:
        # 1. Send Ping
        msg = f"PING at {time.strftime('%H:%M:%S')}"
        ser.write(msg.encode('utf-8'))
        log_to_file(f"SENT: {msg}")

        # 2. Wait for Reply
        time.sleep(1)
        if ser.in_waiting > 0:
            raw = ser.read(ser.in_waiting)
            reply = raw.decode('utf-8', errors='ignore').strip()
            log_to_file(f"REPLY RECEIVED: {reply}")
        else:
            log_to_file("REPLY TIMEOUT: No response from Slave.")
        
        time.sleep(2) # Gap between tests

except KeyboardInterrupt:
    log_to_file("--- MASTER STOPPED ---")
    ser.close()

