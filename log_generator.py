from datetime import datetime
import time
import random

levels = ["ERROR", "WARNING", "INFO", "DEBUG", "TRACE", "ALERT"]

with open("app.log", "a") as f:
	now = datetime.now()
	timestamp = now.strftime('%Y-%m-%d %I:%M:%S%p')
	f.write(f"\n--- Log started at {timestamp} ---\n")

try:
	while True:
	    now = datetime.now()
	    timestamp = now.strftime('%Y-%m-%d %I:%M:%S%p')
	    log = f"{timestamp} - {random.choice(levels)} - Sample log"

	    with open("app.log", "a") as f:
	        f.write(log + "\n")

	    print(log)
	    time.sleep(3)

except KeyboardInterrupt:
	print("\nStopped log generation...")