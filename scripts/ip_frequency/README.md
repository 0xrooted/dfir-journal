## 📘 IP EXTRACTOR 

This script extracts all log entries containing IP address information and
saves them into a separate file for focused analysis.

## Purpose

To detect:
- Brute-force login attempts
- Repeated access from a single IP address
- Potential attacker or scanning IPs

## How It Works

- Reads the log file line by line
- Extracts IP addresses from log entries
- Counts how many times each IP appears
- Displays a frequency report in the console

## Usage

```bash
python ip_frequency.py
