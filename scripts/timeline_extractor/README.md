# Timeline Extractor

This script extracts timestamps from log files and generates a chronological
timeline of events, which is a critical step in Digital Forensics and Incident
Response (DFIR).

## Purpose

To reconstruct the sequence of events during an incident by organizing log
entries based on their timestamps.

Timelines help investigators understand:
- When an attack started
- How events progressed
- Which actions occurred before and after a compromise

## How It Works

- Reads the log file line by line
- Uses regular expressions to identify timestamps
- Writes timestamped log entries to a timeline file

## Usage

```bash
python timeline_extractor.py
