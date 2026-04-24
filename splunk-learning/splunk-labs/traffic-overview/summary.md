# Web Traffic Overview using Splunk

In this exercise, I ingested Apache web server access logs into Splunk using the `access_combined` sourcetype and stored them in a dedicated index named `web_logs`.

The first step was to understand the structure of the logs and identify key fields such as client IP, HTTP method, requested URI, status codes, and user-agent. These fields form the foundation of any web log investigation.

Using SPL queries, I analyzed:

- Number of unique visitors to the website
- Most active IP addresses (Hits by ips)
- Distribution of HTTP status codes
- Frequently accessed URLs
- Difference between normal user behavior and automated traffic

This helped me establish a baseline of what normal traffic looks like, which is a critical step before identifying any suspicious activity.

This process reflects how a SOC analyst begins log analysis in real environments — by first understanding traffic patterns before jumping to conclusions.