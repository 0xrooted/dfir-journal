# Log Scanner

This tool scans log files for suspicious keywords commonly observed during
security incidents.

## Purpose

To quickly identify potentially malicious or abnormal events such as:
- Failed login attempts
- Access denied events
- System errors

## How It Works

- Reads a log file line by line
- Matches predefined suspicious keywords
- Writes matching log entries to an output file

## Keywords Used

- failed
- error
- denied

## Usage

```bash
python log_scanner.py
