# Bruteforce CSV REPORT GENERATOR (what it do)

A small utility that ingests CSV logs of authentication attempts, consolidates entries, and produces summary reports highlighting brute‑force activity (top source IPs, targeted accounts, attempt counts, time windows, and success/failure rates).

# Purpose

Provide analysts and automated tooling with a quick, structured summary of suspected brute‑force campaigns from raw CSV exports so incidents can be triaged, blocked, and investigated faster.

## How it Works

- Load one or more CSV files containing authentication events (timestamp, source IP, username, result, etc.)
- Normalize timestamps and field names, filter relevant event types
- Aggregate by source IP, target account, and time windows
- Compute metrics (attempt counts, successes, failure rates, first/last seen)
- Output summary as CSV/JSON and optional human-readable report for analysts
- CLI flags allow time range, top-N filters, and output format selection


```bash
python incident_report_generator.py

