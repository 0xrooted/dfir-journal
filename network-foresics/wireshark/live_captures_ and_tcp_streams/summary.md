# Lesson 02 – Live Capture & TCP Streams (DFIR Perspective)

## Objective
Perform live network capture and analyze network conversations using display filters and TCP streams.

## Live Capture
- Correct interface selection is critical
- Active interface shows continuous traffic
- Short captures (10–15 seconds) are sufficient for analysis

## Common Display Filters Used
- dns      → View DNS queries and responses
- http     → View HTTP traffic
- tcp      → View TCP-based traffic
- ip.addr == x.x.x.x → Track specific IP communication

Display filters allow focused investigation without deleting evidence.

## TCP Stream Analysis
Using:
Right-click → Follow → TCP Stream

This reconstructs the full client-server conversation and helps in:
- Understanding request/response flow
- Identifying file downloads
- Observing authentication or data transfer

## Readable vs Unreadable Streams
- Readable headers with unreadable body often indicate binary data (files, certificates)
- Unreadable streams with TLS indicate encrypted traffic
- Binary data ≠ Encrypted data

## Real Observation
A certificate file (.der) was downloaded from a trusted Let's Encrypt domain.
This behavior was identified as normal browser activity.

## DFIR Insight
Not all complex-looking traffic is malicious.
Normal traffic must be understood first to identify anomalies.

## Key Learning
DFIR analysis focuses on:
- Behavior
- Patterns
- Context

Readable content is helpful, but behavior is more important than payload visibility.
