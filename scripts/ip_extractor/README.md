# IP Log Extractor

This script extracts all log entries containing IP address information and
saves them into a separate file for focused analysis.

## Purpose

To isolate network-related activity from large log files, which helps during:
- Network intrusion investigations
- Brute-force detection
- Suspicious external connections analysis

## How It Works

- Reads the log file line by line
- Identifies entries containing IP information
- Writes matching log entries to an output file

## Usage

```bash
python ip_extractor.py
