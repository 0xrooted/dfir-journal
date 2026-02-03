# Understanding EDR

This small project was created to understand how Endpoint Detection and Response (EDR) tools work from an analyst’s point of view.

Instead of learning any specific EDR product, the focus here was to understand the behavior and patterns that EDR tools monitor on endpoints. The practice was done by generating real process activity on Windows and Linux systems and observing how such actions would appear inside an EDR console.

The goal was to build an investigation mindset by simulating suspicious command execution, file downloads, and process spawning — similar to what happens during real attacks.

This helped in understanding:

- How process trees are formed
- Why PowerShell and bash are commonly abused
- How download and execution patterns are detected
- How parent-child process relationships help in identifying malicious behavior
- How system logs (like Event Viewer) act as the base data for EDR tools

This project represents a practical approach to learning EDR concepts without access to enterprise EDR software, by focusing on the core behavior that such tools monitor.