# Splunk Investigation Lab Series (SOC / DFIR Practice)

This repository contains hands-on investigations performed using Splunk as a SIEM platform.

The goal of these labs is not just to run queries, but to develop real incident investigation skills used in SOC and DFIR roles.

All investigations are done on raw log data by simulating how security analysts work in real environments.

---

## What this project demonstrates

Through these labs, the following practical skills are developed:

- Understanding how logs are structured and ingested in Splunk
- Creating indexes and using proper sourcetypes
- Writing SPL queries to extract meaningful information
- Identifying suspicious patterns from normal traffic
- Detecting malicious behavior from web logs
- Differentiating legitimate bots from attackers
- Tracking attacker activity across multiple events
- Investigating sensitive file access attempts
- Building an investigation mindset instead of random searching

---

## Investigation Approach

Each investigation follows a proper analyst workflow:

1. Observe the logs
2. Identify patterns
3. Ask investigative questions
4. Write queries to validate assumptions
5. Identify suspicious entities (IPs, user agents, URIs)
6. Draw conclusions based on evidence from logs

---

## Folder Structure

Each folder represents a specific investigation scenario.

Inside every folder:

- `summary.md` – Explanation of the investigation, queries used, and findings
- Screenshots – Raw query outputs from Splunk during analysis

---

## Skills Practiced in this Repository

This work reflects practical experience in:

- SIEM usage (Splunk)
- Log analysis
- Web log investigation
- Threat hunting basics
- SOC investigation workflow
- DFIR mindset development

---

## Note on Screenshots

Screenshots are taken directly during the investigation process without modifying any data. They represent real query outputs and observations made during the lab.

---

## Purpose

This repository is part of continuous practice to become job-ready for SOC / DFIR roles by working with logs the same way analysts do in real security teams.