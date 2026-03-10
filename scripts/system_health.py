import psutil
import logging

# Setup logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_system_health():
    # Check CPU
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        print(f"ALERT: High CPU usage detected: {cpu_usage}%")
        logging.warning(f"High CPU usage: {cpu_usage}%")

    # Check Memory
    memory = psutil.virtual_memory()
    if memory.percent > MEMORY_THRESHOLD:
        print(f"ALERT: High Memory usage detected: {memory.percent}%")
        logging.warning(f"High Memory usage: {memory.percent}%")

    # Check Disk Space
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        print(f"ALERT: Low Disk Space: {disk.percent}% used")
        logging.warning(f"Low Disk Space: {disk.percent}%")

    print("System check complete. Check 'system_health.log' for details.")

if __name__ == "__main__":
    check_system_health()