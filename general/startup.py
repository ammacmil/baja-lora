import serial
import time
import os

# --- Configuration ---
PORT = '/dev/serial0' 
BAUD = 9600
LOG_FILE = "connection_log.txt"
CONFIG_FILE = "config.txt"

def get_mode_from_config():
    """Reads config.txt to determine if we are 'master' or 'slave'."""
    if not os.path.exists(CONFIG_FILE):
        print(f"Error: {CONFIG_FILE} not found! Defaulting to slave.")
        return "slave"
    
    with open(CONFIG_FILE, "r") as f:
        content = f.read().lower()
        if "master" in content:
            return "master"
        else:
            return "slave"

def log(message):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    entry = f"[{timestamp}] {message}"
    print(entry)
    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")

def run_master(ser):
    log("--- MODE: MASTER (PING) ---")
    try:
        while True:
            ping_msg = f"PING_{int(time.time())}"
            ser.write(ping_msg.encode('utf-8'))
            log(f"SENT: {ping_msg}")

            time.sleep(1.5) 
            if ser.in_waiting > 0:
                raw = ser.read(ser.in_waiting)
                reply = raw.decode('utf-8', errors='ignore').strip()
                log(f"RCVD: {reply}")
            else:
                log("STAT: No reply (Timeout)")

            time.sleep(2)
    except KeyboardInterrupt:
        log("Master Stopped.")

def run_slave(ser):
    log("--- MODE: SLAVE (PONG) ---")
    try:
        while True:
            if ser.in_waiting > 0:
                raw = ser.read(ser.in_waiting)
                incoming = raw.decode('utf-8', errors='ignore').strip()
                log(f"RCVD: {incoming}")

                response = f"PONG_REPLY_TO_{incoming}"
                ser.write(response.encode('utf-8'))
                log(f"SENT: {response}")
            
            time.sleep(0.1)
    except KeyboardInterrupt:
        log("Slave Stopped.")

# --- Main Execution ---
if __name__ == "__main__":
    # 1. Determine Role
    role = get_mode_from_config()
    
    # 2. Initialize Serial
    try:
        ser = serial.Serial(PORT, BAUD, timeout=1)
        ser.reset_input_buffer()
        
        # 3. Start Function based on Role
        if role == "master":
            run_master(ser)
        else:
            run_slave(ser)
            
    except Exception as e:
        print(f"Critical Error: {e}")
    finally:
        if 'ser' in locals():
            ser.close()

