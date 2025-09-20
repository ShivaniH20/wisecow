from collections import Counter
import re

# --- Step 1: Define the log file ---
log_file = "access.log"

# --- Step 2: Prepare counters ---
status_counter = Counter()
page_counter = Counter()
ip_counter = Counter()

# --- Step 3: Read the log file ---
with open(log_file, "r") as f:
    for line in f:
        # Example line: 127.0.0.1 - - [20/Sep/2025:14:00:05 +0000] "GET /home HTTP/1.1" 404 512
        match = re.match(r'(\d+\.\d+\.\d+\.\d+) .* "(?:GET|POST) (.*?) HTTP/.*" (\d+)', line)
        if match:
            ip, page, status = match.groups()
            status_counter[status] += 1
            page_counter[page] += 1
            ip_counter[ip] += 1

# --- Step 4: Print summary ---
print("===== Log Analysis Report =====")
print(f"Total 404 errors: {status_counter.get('404', 0)}")
print("Top 3 requested pages:")
for page, count in page_counter.most_common(3):
    print(f"{page} -> {count} requests")

print("Top 3 IP addresses making requests:")
for ip, count in ip_counter.most_common(3):
    print(f"{ip} -> {count} requests")
