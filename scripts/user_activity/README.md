# User Activity Counter

This script analyzes log files to determine how frequently a specific user
appears during system activity.

## Purpose

To help identify:
- Compromised user accounts
- Excessive or abnormal user activity
- Privileged account misuse

## How It Works

- Prompts the investigator to enter a username
- Scans the log file for matching user entries
- Counts and reports the number of occurrences

## Usage

```bash
python user_activity_counter.py
