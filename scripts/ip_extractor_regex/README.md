
# Regex IP Extractor

This script extracts IP addresses from log files using regular expressions and
stores them in a separate file for further analysis.

## Purpose

To identify all IP addresses involved in system or network activity, which can
be used for:
- Brute-force detection
- Network intrusion analysis
- Threat intelligence correlation

## How It Works

- Reads the log file line by line
- Uses a regex pattern to detect valid IPv4 addresses
- Writes each extracted IP address to an output file

## Usage

```bash
python ip_extractor.py