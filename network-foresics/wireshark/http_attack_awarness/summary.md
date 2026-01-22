# Lesson 4 – HTTP Attack Awareness (Quick Recap)

This lesson focuses on identifying common web attack patterns through HTTP traffic
and server access logs.

Covered attack patterns:
- SQL Injection (`' OR 1=1`, `UNION SELECT`)
- Directory Traversal (`../`, `../../etc/passwd`)
- Command Injection (`;whoami`, `|id`)
- Suspicious script access (`shell.php`, `cmd.php`)

Key takeaway:
HTTP-based attacks often look like normal requests.
The attack signal is usually hidden in:
- URL paths
- Query parameters
- Repeated attempts from the same IP

This topic was already implemented practically in:
web-attack-log-detector project.
