# Brute Force CSV Report Generator

This script analyzes authentication-related log entries and generates a
structured CSV report highlighting potential brute-force attacks based on
failed login attempts.

## Purpose

To convert raw log data into a structured CSV report that can be:
- Reviewed manually
- Shared with SOC teams
- Imported into SIEM or Excel for further analysis

## How It Works

- Reads the log file line by line
- Identifies failed authentication attempts using keywords
- Extracts IPv4 addresses using regular expressions
- Counts failed attempts per IP address
- Applies a threshold to determine brute-force activity
- Writes results into a CSV report

## Detection Logic

An IP address is flagged as suspicious if:

