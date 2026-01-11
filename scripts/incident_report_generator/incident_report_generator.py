from  datetime import datetime
import csv 
import os

BRUTREFORCE_CSV = "examples/bruteforce_report.csv"
SUSPICIOUS_CSV = "examples/suspicious.log"
TIMELINE_CSV = "examples/timeline.txt"
IP_FILE = "examples/ip_extracted_regex.log"

OUTPUT_REPORT = "examples/incident_report.txt"

def file_exists (Path):
    return os.path.exists(Path)

with open (OUTPUT_REPORT, "w") as report:

    report.write("Incident Report\n")
    report.write ("="*50 +"\n")
    report.write(f"Report Generated on: {datetime.now()}\n\n") 

    report.write ("2. Incident Summary\n")

    report.write (
        "- Multiple Suspecious Activites were detected across systems.logs\n"

        "- Indications suggest possible brute-force attacks attemtpted.\n"
    )

    report.write ("2. Indicators of Compromise (IOC)\n")

    if file_exists (IP_FILE):
        unique_ips= set()
        with open (IP_FILE, "r") as ip_file:
            for line in ip_file:
                unique_ips.add (line.strip())

            for ip in unique_ips:
                report.write (f"- {ip}\n")
            else:
                report.write ("- IP Extraction output not available\n")
                report.write ("\n")

    report.write ("3. Brute-Force Attack Details\n")
    
    if file_exists (BRUTREFORCE_CSV):
        with open (BRUTREFORCE_CSV, "r") as csvfile:
            reader = csv.reader (csvfile)
            next (reader, None)  

            for row in reader:
                ip, attempts, status = row
                if status  =="YES":
                    report.write (f"- IP: {ip} Exceeds Failed Logins | Attempts: {attempts}\n")
    else:
        report.write ("- Brute-Force CSV report not available\n")

    report.write ("4 Timeline of events \n")
    if file_exists (TIMELINE_CSV):
        with open (TIMELINE_CSV, "r") as timeline_file:
            for line in timeline_file:
                report.write (line)
    else:
        report.write ("- Timeline file not available\n")
        report.write ("\n")

        report.write ("5. Analyst Conclusion\n")
        report.write
        (
        "Based on correlated evidence from multiple analysis scripts, "
        "the observed activity is consistent with a brute-force attack "
        "attempt. It is recommended to block offending IP addresses, "
        "review affected user accounts, and retain logs for further investigation.\n"
        )
        print ("[+] Incident report generated {OUTPUT_REPORT}")