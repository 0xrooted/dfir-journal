# Detecting Suspicious Web Activity in Splunk

After establishing the traffic baseline, the next step was to identify abnormal patterns that may indicate scanning or exploitation attempts.

By focusing on 404 status codes and unusual user-agents, I identified IP addresses attempting to access non-existing and sensitive paths such as:

- /admin
- /phpmyadmin
- /config.php
- /etc/passwd
- hidden and secret directories

Using SPL, I detected clients generating a high number of 404 errors and accessing many unique URLs in a short time span. This is a common indicator of directory brute-forcing or automated scanning tools.

User-agent analysis also revealed tools like `curl` and `sqlmap`, which are typically associated with reconnaissance and exploitation.

This exercise demonstrates how Splunk can be used to quickly identify scanning behavior and potential attackers using simple but effective queries.