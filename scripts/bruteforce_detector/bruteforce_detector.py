import re
from collections import defaultdict

log_file = "../data/sample.log"
threshold = 2 

keywords = ["failed password", "failed login", "failed attempt"]

ip_pattern = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"

failed_attempts = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        line_lower = line.lower()
        if any(word in line_lower for word in keywords):
            ip_match = re.search(ip_pattern, line)
            if ip_match:
                ip = ip_match.group()
                failed_attempts[ip] += 1

print (" === Brute Force Detection Report === ")
for ip, count in failed_attempts.items():
    if count >= threshold:
        print(f"[ALERT] {ip} → {count} failed attempts")
