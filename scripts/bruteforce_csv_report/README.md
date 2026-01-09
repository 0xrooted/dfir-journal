# Bruteforce CSV Report Generator

Ever wondered which IP addresses are hammering your systems with failed login attempts? This tool does the detective work for you! It scans log files, finds all those suspicious repeated failed login attempts, and creates a neat CSV report so you can see exactly which IPs are acting fishy.

# Purpose

When someone tries to break into a system through brute force attacks (repeatedly trying passwords), they leave a trail in the logs. This tool helps security analysts quickly spot these attackers without having to read through thousands of log lines manually. It's like having a spotlight that points directly at the bad actors.

## How it Works

Think of it as a three-step process:

1. **Read and hunt** - The script goes through your log file and hunts for red flags like "failed passwords", "failed login", or "failed attempts"
2. **Grab the IP addresses** - When it finds a suspicious line, it extracts the IP address from it
3. **Count the damage** - It tallies up how many failed attempts came from each IP
4. **Generate the report** - Finally, it creates a CSV file that shows:
   - Which IP addresses were causing trouble
   - How many failed attempts each one made
   - Whether it looks like a brute force attack (if there are 2 or more attempts, it flags it as "Yes")

That's it! You get a clean, organized report ready for analysis.


```bash
python bruteforce_csv_report.py