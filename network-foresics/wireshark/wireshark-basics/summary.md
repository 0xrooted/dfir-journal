# Lesson 01 – Wireshark Basics (DFIR Perspective)

## Objective
Understand what Wireshark is, how it works internally, and how it is used in DFIR for network evidence analysis.

## What is Wireshark?
Wireshark is a network packet analyzer that captures and displays network traffic at the packet level.
In DFIR, it is used to analyze evidence left behind by network communications.

## Key DFIR Concept
Wireshark is NOT a hacking tool.
It is a forensic and investigative tool used to:
- Observe network behavior
- Analyze traffic patterns
- Reconstruct timelines

## Packet Structure (High Level)
Each packet contains multiple layers:
- Frame
- Ethernet
- IP
- TCP / UDP
- Application Data (HTTP, DNS, etc.)

DFIR analysis focuses on understanding these layers to answer:
Who communicated, when, how, and with whom.

## Capture vs Display Filters
- Capture Filters:
  - Applied before capture
  - Discard packets permanently
  - Avoided in DFIR to prevent evidence loss

- Display Filters:
  - Applied after capture
  - Do not delete data
  - Preferred method in DFIR

## Important UI Areas
- Interface selection (critical)
- Packet list (timeline)
- Packet details (layer breakdown)
- Packet bytes (raw evidence)

## Key Learning
In DFIR:
Capture everything.
Filter later.
Never lose evidence.
