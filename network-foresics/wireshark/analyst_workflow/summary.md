# Lesson 8 – DFIR Network Analyst Workflow

## Objective
To understand how DFIR analysts investigate network traffic in a structured and practical way, focusing on reasoning and conclusions rather than just tools.

---

## Core Idea
In DFIR, packets are not the goal — **decisions are**.

Wireshark and other tools are used to support analysis, not to blindly inspect traffic.

---

## The DFIR Network Analysis Workflow

### 1. Trigger
Every investigation starts with a reason.

Common triggers include:
- Suspicious outbound traffic
- SOC or EDR alert
- User-reported issue
- Incident response escalation

An analyst does not start without a trigger.

---

### 2. Scope
Define clear boundaries for the investigation.

This includes:
- Affected host or user
- Time window
- Relevant protocols

Scoping prevents unnecessary analysis and reduces noise.

---

### 3. Triage
Initial high-level inspection to separate normal from abnormal traffic.

Common filters used:
- `dns`
- `http`
- `tls`

The goal is to quickly understand traffic patterns before deep analysis.

---

### 4. Hypothesis
Based on triage, the analyst forms an initial assumption.

Examples:
- Traffic appears browser-generated
- Destination domain looks legitimate
- Client behavior does not match a normal browser

A hypothesis can be wrong and is expected to be validated.

---

### 5. Validation
Evidence is collected to support or reject the hypothesis.

This may include:
- DNS queries and responses
- TLS handshake details
- SNI extraction
- Cipher suite and extension analysis
- Timing and connection behavior

At this stage, tools like Wireshark are heavily used.

---

### 6. Conclusion
The analyst produces a clear and concise outcome.

Possible conclusions:
- Traffic is benign
- Traffic is suspicious and requires escalation
- No sufficient evidence of malicious activity

Conclusions should be factual, not speculative.

---

## Key DFIR Principles
- Encrypted traffic is not automatically malicious
- Not all investigations lead to incidents
- Analysts stop once sufficient evidence is gathered
- Clear reasoning is more important than deep packet inspection

---

## Role of Wireshark
Wireshark is primarily used for:
- Manual validation
- Deep inspection of specific packets
- Understanding protocol behavior

It is not a detection or alerting tool.

---

## Key Takeaway
A DFIR analyst follows a structured workflow:  
**Trigger → Scope → Triage → Hypothesis → Validation → Conclusion**

This approach ensures efficient, accurate, and defensible investigations.