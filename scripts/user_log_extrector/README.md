# User Log Extractor

This script extracts all log entries related to a specific user and saves them
into a separate file for focused analysis.

## Purpose

To isolate user-specific activity during investigations involving:
- Account compromise
- Insider threats
- Privilege misuse

## How It Works

- Takes a username as input
- Scans the log file for matching entries
- Writes all related logs to an output file

## Usage

```bash
python user_log_extractor.py