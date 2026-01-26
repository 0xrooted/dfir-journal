# Lesson 7 – JA3 Fingerprinting (Wireshark Perspective)

## Objective
To understand what JA3 is, why it is used in DFIR, and how its building blocks can be analyzed manually using Wireshark even when traffic is encrypted.

---

## What is JA3?
JA3 is a TLS client fingerprinting technique.  
It identifies a client based on how it behaves during the TLS handshake, rather than what data it sends.

JA3 does **not** inspect payload content.  
Instead, it fingerprints the **TLS Client Hello** message.

---

## Why JA3 Exists
Modern network traffic is mostly encrypted (HTTPS/TLS).  
This makes payload inspection ineffective for DFIR analysts.

JA3 solves this by focusing on **client behavior**, which remains visible before encryption starts.

---

## What JA3 is Built From
JA3 is derived from five fields inside the TLS Client Hello:

1. TLS Version  
2. Cipher Suites  
3. Extensions  
4. Supported Elliptic Curves  
5. EC Point Formats  

These fields are combined in a fixed order and hashed (MD5) by tools like Zeek or Suricata.

---

## Role of Wireshark
Wireshark does **not** generate JA3 hashes.

Wireshark is used to:
- Identify the TLS Client Hello
- Manually inspect JA3-related fields
- Understand whether traffic looks browser-like or suspicious

This manual analysis is important for DFIR learning and investigations.

---

## Practical Analysis in Wireshark
Steps followed:
1. Apply `tls` display filter
2. Locate a `Client Hello` packet
3. Expand:
   - Transport Layer Security
   - Handshake Protocol: Client Hello
4. Observe:
   - TLS version used
   - Number and type of cipher suites
   - Number and type of extensions
   - Supported elliptic curves

---

## Analyst Observations
- Browsers usually present:
  - Modern TLS versions
  - Long cipher suite lists
  - Multiple extensions (SNI, ALPN, supported groups, etc.)

- Malware or automated tools often show:
  - Limited cipher suites
  - Few or missing extensions
  - Older or unusual TLS configurations

---

## JA3 vs SNI
- SNI tells **where** the client is connecting (domain name)
- JA3 tells **how** the client behaves during TLS handshake

Both are used together in DFIR investigations.

---

## DFIR Use Cases
- Detecting encrypted Command-and-Control traffic
- Identifying non-browser clients on endpoints
- Threat hunting using known malicious JA3 fingerprints
- Supporting incident response decisions

---

## Key Takeaway
Even when traffic is encrypted, TLS handshake metadata such as JA3 allows analysts to make informed security judgments based on client behavior.

JA3 is a behavior-based signal, not a content-based one.