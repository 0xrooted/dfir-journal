# SOC Investigation LAb using Splunk (Web + Auth +Auth + Syslog Correlation)

This lab demonstrates how multiple log sources are correlated in Splunk to reconstruct an attack story from reconnaissance to post-exploitation.

The investigation was perfromed using three diffrent types of logs:

- Web server access logs
- Linux SSH authentication logs
- System logs (syslog)

All logs are belong to same simulated environment where a single attacker intracts with the infrastructure 

---

## Objective

The goal of this investigation was to:

- Identify a suspecious xternal IP from web logs 
- Verify if the same IP attempt SSH access
- Confrim whether the attacker gained access
- Observe system-level actions performed after login
- Reconstruct the full attack timeline using Splunk

This mimics how real SOC analyst innvestigate alerts.

---

## Log Sources Used

| Log Type | Index | Sourcetype | Purpose |
|----------|-------|------------|---------|
| Web Access Logs | `web_logs` | `access_combined` | Detect reconniaissance and probing attempts |
| Linux Auth Logs | `linixx_logs` | `linux_secure` | Detect SSH brute force and login attempts |
| System Logs | `sys_logs` | `syslog` | Detect post-exploitation activity |

---

## Investigation Phase

### Phase 1 - Web Reconniaissance 

The first step was to indetify abnormal traffic from web traffic.

**Query Used**

`index=web_logs | stats cunt by clientip | sort - count`

This help idetify the most active IP making suspicious reqests.

Further analysis:

`index= web_logs clientip=ATTACKER_IP| table _time uri status useragent`

Suspecious idicators observed:

- Access attempts to `/admin`, `/etc/password`, `/phpmyadmin`
- Use of `curl` user agent 
- Repeated failed login attempts


---

### Phase 2 - SSH Brute Force Attempt

The same IP was checked in authentication logs,

`index=linux_logs ATTACKER_IP "Failed password"`


Indicators:

- Multiple failed login attempts
- Attempts using different usernames

Then checked for successful access:


`index=linux_logs ATTACKER_IP "Accepted password"`


This confirmed the attacker gained SSH access.

---

### Phase 3 - Post Exploitation Activity

System logs were analyzed to observe what actions were taken after login.

**Query used:**


`index=sys_logs ATTACKER_IP`


Suspicious commands identified:

- `wget` used to download payload
- `chmod +x` to make it executable
- `nc` reverse shell attempt
- Cron job activity

---

### Phase 4 - Building the Attack Timeline

To reconstruct the complete sequance of events:

`index=* ATTACKER_IP | sort-time`

1. Website probing 
2. SSH brute force attempts
3. Succesfull login
4. Malware download
5. Reverse shell execution

---


### Key Learning Outcomes

This lab helped understand:

- How diffent logs tell diffrent parts of the same story 
- How to correlate logs across musltiple indexes 
- Identiifying reconnianssance, brute force, and post-exploitation patterns
- Using SPL commands like `stats`, `table`, `sort`, and filters for investigation 
- Real-world SOC investigation workflow using Splunk

---

### Why This Lab Matters

This is not simple log searching.
This is a practical demonstration of ow SOC analysts investigate real incidents using splunk by corelating multiple log sources to trace attacker behaviour

This covers a significant portion of real entry-level SOC work