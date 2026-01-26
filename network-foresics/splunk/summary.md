# Splunk Fundamentals – SOC Analyst Summary

## Overview
This repository documents my hands-on learning of Splunk from a Security Operations Center (SOC) and DFIR perspective. The focus is on understanding how Splunk is used in real-world environments to analyze logs, correlate events, and detect suspicious or malicious activity using practical datasets instead of toy examples.

---

## What is Splunk?
Splunk is a data analysis platform that collects, indexes, and makes machine-generated data searchable. It does not generate logs or automatically stop attacks. Instead, it provides analysts with the capability to investigate large volumes of logs efficiently and derive security insights.

Splunk is widely used in SOC environments because it enables centralized log analysis and event correlation across multiple systems.

---

## Why Splunk is Used in SOC Environments
Organizations generate logs from many different sources such as:
- Host-based systems (Linux, Windows)
- Servers and applications
- Network and security devices

These logs are often distributed, noisy, and difficult to analyze manually. Splunk centralizes this data, extracts useful fields, and allows analysts to correlate events across sources to identify security incidents.

---

## Log Centralization and Normalization
Splunk collects logs from multiple sources and processes them to make them searchable and comparable. While logs may originate in different formats, Splunk extracts relevant fields such as IP addresses, usernames, timestamps, and request paths to support effective analysis and investigation.

---

## Log Correlation
Log correlation is the process of linking related events from multiple log sources to identify meaningful security patterns.

For example:
- A firewall log shows repeated connections from an IP
- A web server log shows multiple login requests from the same IP
- Authentication logs show repeated failed login attempts

When analyzed together, these events indicate a potential brute-force attack.

---

## Role of the Analyst
Splunk itself is not a security brain. The analyst is responsible for:
- Writing search queries (SPL)
- Interpreting log patterns
- Identifying false positives
- Making investigation and escalation decisions

Splunk provides the platform, but detection logic and investigation come from the analyst.

---

## Practical Focus
This project emphasizes:
- Working with realistic log datasets
- Understanding how raw logs translate into security insights
- Building confidence to handle unfamiliar logs in real job or internship environments
- Developing an investigation-first mindset rather than relying on automation