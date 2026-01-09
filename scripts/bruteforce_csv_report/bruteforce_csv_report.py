import re
import csv
from collections import defaultdict

log_file = "../data/sample.log"
output_csv = "bruteforce_report.csv"

threshold = 2

keywords = ["failed passwords", "failed login", "failed attempts"]

ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
failed_attempts = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        line_lower = line.lower()
        if any (keyword in line_lower for keyword in keywords):
            ip_match = re.search(ip_pattern, line)
            if ip_match:
                ip = ip_match.group()
                failed_attempts [ip] += 1

with open (output_csv, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Ip Address", "Failed Attempts", "Bruteforce Detected"])

    for ip, count in failed_attempts.items():
        status = "Yes" if count >= threshold else "No"
        writer.writerow([ip, count, status])

print ("[+] CSV report generated: ", output_csv)