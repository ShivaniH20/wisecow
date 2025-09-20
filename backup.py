import os
import shutil
from datetime import datetime

source = "C:/wisecow/data"       # folder to backup
destination = "C:/wisecow/backup"  # backup folder
log_file = "backup.log"           # log file

try:
    shutil.copytree(source, destination)
    status = "Backup successful"
except Exception as e:
    status = f"Backup failed: {e}"

with open(log_file, "a") as log:
    log.write(f"{datetime.now()} - {status}\n")

print(status)
