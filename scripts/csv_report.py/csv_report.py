import re
import csv
from collections import defaultdict

log_file = "../data/sample.log"
output_csv = "bruteforce_report.csv"

threshold = 2  

keywords = [ "failed password","failed login","failed attempt" ]

ip_pattern = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"

failed_attempts = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        line_lower = line.lower()
        if any(keyword in line_lower for keyword in keywords):
            ip_match = re.search(ip_pattern, line)
            if ip_match:
                ip = ip_match.group()
                failed_attempts[ip] += 1

with open(output_csv, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["IP Address", "Failed Attempts", "Brute Force Detected"])

    for ip, count in failed_attempts.items():
        status = "YES" if count >= threshold else "NO"
        writer.writerow([ip, count, status])

print("[+] CSV Brute Force Report Generated:", output_csv)
