# Lesson 5 – DNS Traffic Analysis (DFIR Perspective)

This lesson changed the way I look at DNS.  
Earlier, DNS felt like a simple “domain to IP” step. Now I see it as one of the
strongest behavioral signals in DFIR.

---

## What normal DNS looks like

In normal browsing:
- DNS queries are short-lived
- Domains are readable and well-known
- Queries happen only when a user action occurs
- DNS stops once the site is loaded

DNS has a purpose and then disappears.

---

## What makes DNS suspicious

While observing DNS traffic, these patterns stood out as red flags:

- Random-looking or very long domain names
- Domains that don’t look human-generated
- Repeated DNS queries to the same domain at fixed intervals
- DNS traffic continuing without any visible user activity
- Unusual query types like TXT being used frequently

Randomness and repetition usually indicate automation, not human behavior.

---

## DNS Tunneling (basic understanding)

DNS can be abused to transfer data by embedding it inside subdomains.

Example pattern:
randomdata1.randomdata2.bad-domain.com

Indicators of DNS tunneling:
- Extremely long subdomains
- High entropy (looks encoded or scrambled)
- Large number of similar DNS queries

DNS is used because it is often allowed through firewalls.

---

## DFIR mindset for DNS analysis

While looking at DNS traffic, I now ask:
- Is this domain known or suspicious?
- Does the structure look human or machine-generated?
- Is this query linked to a user action?
- Is the frequency normal or constant?

If I cannot clearly explain the “why” behind a DNS query, it deserves investigation.

---

## Key Takeaways

- DNS is not just a helper protocol, it is a detection signal
- Randomness + repetition is more important than the domain name itself
- Encrypted traffic can still leak behavior through DNS
- DNS analysis is critical for malware and C2 detection