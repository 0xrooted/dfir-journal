# Brute Force Detector

This script detects repetitive failed authentication attempts from log files
to identify potential brute-force attacks based on source IP addresses.

## Purpose

To detect suspicious login behavior where an IP address exceeds a defined threshold of failed 
authentication attempts, indicating a possible brute-force attack.

## How It Works

- Reads the log file line by line
- Searches for failed authentication keywords
- Extracts IPv4 addresses using regular expressions
- Counts failed attempts per IP address
- Flags IPs that cross the configured threshold

## Detection Logic

An IP address is marked suspicious if:
-Failed Attempts >= Threshold

## Usage

```bash
python bruteforce_detector.py