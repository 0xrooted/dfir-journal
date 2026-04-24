# Splunk Monitoring Lab

## Objective

Simulate a basic SOC investigation using web, linux and system logs.
The goal was to perform detection, correlation, alert creation and dashboard monitoring

---

# Log Sources Used

- Web Server Access Logs (index: web_logs)
- Linux Authentication Logs (index: linux_logs)
- System Logs / Syslog (index: sys_logs)

---

## Investigation Phases

### Phase 1 – Web Reconnaissance Detection

Suspicious web activity was identified by detecting access attempts to sensitive paths:

- /admin
- /etc/passwd
- /phpmyadmin

Query used:

`index=web_logs uri="/admin" OR uri="/etc/passwd" OR uri="/phpmyadmin"`


Findings:
- Suspicious IP identified
- Repeated probing of sensitive resources
- Indicators of reconnaissance behavior

---

### Phase 2 – Authentication Log Review

Linux authentication logs were analyzed to detect SSH brute force attempts.

Query used:

`index=linux_logs "Failed password"`


No significant repeated failed login attempts were observed in the dataset.

---

### Phase 3 – Post-Exploitation Activity

System logs were analyzed to detect potentially malicious command execution.

Query used:

`index=sys_logs wget OR nc OR chmod`


Findings:
- Suspicious command execution detected
- Possible payload download attempt
- Indicators of post-compromise activity

---

## Detection & Monitoring

Basic alerts were configured for:

- Web reconnaissance attempts
- SSH brute force detection
- Suspicious system command execution

A monitoring dashboard was created to visualize activity across all indexes.

---

## Skills Demonstrated

- Log ingestion and index management
- Field-based filtering and search
- Multi-index correlation
- Attack timeline reconstruction
- Basic detection engineering
- Alert configuration in Splunk
- SOC-style documentation

---

## Conclusion

This lab simulates a real-world SOC investigation workflow, demonstrating how multiple log sources can 