# Lesson 6 – Encrypted Traffic Analysis (TLS / SNI)

## Objective
Understand how to analyze **encrypted HTTPS traffic** in Wireshark and extract **useful intelligence without decrypting payloads**, focusing on **SNI (Server Name Indication)**.

This lesson proves that:
- 🔒 HTTPS traffic can still leak **valuable metadata** for DFIR and threat hunting.

---

## Key Concepts Learned

### 1. HTTPS ≠ Fully Invisible
Even when payload is encrypted:
- IP addresses
- Ports (443)
- TLS handshake details
- Server Name (SNI)
are often **visible**.

Attackers rely on this misconception.

---

### 2. What is SNI?
**SNI (Server Name Indication)** is part of the **TLS Client Hello** message.

It tells the server:
> “Which domain I am trying to connect to”

This is required because:
- One IP can host multiple domains
- TLS cert selection depends on hostname

---

### 3. Where SNI Exists
- Only in **TLS Handshake**
- Specifically inside **Client Hello**
- Not present in encrypted application data

📌 If you miss Client Hello → you miss SNI.

---

## Practical Steps (Wireshark)

### Step 1: Capture Traffic
- Interface: Wi-Fi / Ethernet
- Visit any HTTPS website in browser

---

### Step 2: Apply Display Filter
- tls
- This shows only TLS packets

---

### Step 3: Find CLient HEllo
- Look for packet with:
- Protocol: TLS
- Info: Client Hello

---

### Step 4: Locate SNI
Expand packet layers:

```
Transport Layer Security
└─ Handshake Protocol: Client Hello
└─ Extensions
└─ Server Name Indication
└─ Server Name: example.com
```

🎯 **This domain is the SNI**

---

## When SNI Analysis is Used (DFIR)

### Incident Response
- Suspicious HTTPS traffic
- Unknown IPs communicating over 443
- Malware using domain-based C2

### Threat Hunting
- Domain-based detections
- Beaconing over TLS
- Bypassing content inspection

### SOC Monitoring
- “Why is this host talking to this domain?”
- Validate suspicious outbound traffic

---

## Important Observations

- Port **443 traffic can still be malicious**
- Trusted websites ≠ always safe
- Certificates can be abused
- Encryption hides content, **not intent**

---

## Limitations of SNI
- Encrypted SNI (ESNI / ECH) is emerging
- Not all traffic exposes SNI
- Modern malware may avoid SNI leakage

Still widely effective **today**.

---

## Evidence / Screenshots (Optional but Recommended)

Add screenshots only if documenting lab work.

Suggested screenshots:
1. TLS packets filtered (`tls`)
2. Client Hello packet selected
3. Expanded SNI field showing domain name

📸 These strengthen DFIR credibility but are **not mandatory**.

---

## DFIR Takeaway
> Even without decrypting traffic, analysts can extract **actionable intelligence** from TLS metadata.

SNI analysis is a **core DFIR skill**, not an advanced trick.