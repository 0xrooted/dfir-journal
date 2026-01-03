import re

input_file = "../data/sample.log"
output_file = "ip_extracted_regex.log"

ip_pattern = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        ips = re.findall(ip_pattern, line)
        for ip in ips:
            outfile.write(ip + "\n")

print("IP Extraction Completed.")
