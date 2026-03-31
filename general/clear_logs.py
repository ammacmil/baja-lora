import os
import time

LOG_FILE = "connection_log.txt"

def reset_log():
    # Check if the file exists before trying to clear it
    if os.path.exists(LOG_FILE):
        try:
            # 'w' mode opens the file for writing and truncates it to zero length
            with open(LOG_FILE, "w") as f:
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                f.write(f"--- LOG RESET ON {timestamp} ---\n")
            
            print(f"Success: {LOG_FILE} has been cleared.")
        except Exception as e:
            print(f"Error clearing file: {e}")
    else:
        print(f"File '{LOG_FILE}' does not exist yet. Nothing to clear.")

if __name__ == "__main__":
    confirm = input("Are you sure you want to clear the connection log? (y/n): ")
    if confirm.lower() == 'y':
        reset_log()
    else:
        print("Aborted. Log file was not changed.")
