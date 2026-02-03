# EDR Behavior Analysis Practice (Windows & Linux)

## Objective
To understand how Endpoint Detection and Response (EDR) tools detect suspicious activity by observing process chains, command execution, and file behavior on both Windows and Linux systems.

---

## Windows Practice

I simulated attacker-like behavior using CMD and PowerShell to understand how malicious activity appears in EDR.

### Activities performed:
- Opened CMD and launched PowerShell from it
- Used PowerShell to download a file from the internet
- Executed the downloaded file using a process
- Observed parent-child process relationships

### Log Observation:
- Used Event Viewer (Event ID 4688) to monitor process creation logs
- Verified how `cmd.exe` spawned `powershell.exe` and then other processes

### Key Learning:
PowerShell downloading a file and executing it forms a suspicious process chain often flagged in EDR.

---

## Linux Practice (Ubuntu WSL)

To map the same concept in Linux:

### Activities performed:
- Used bash terminal
- Downloaded a file using `wget` / `curl`
- Changed file permissions using `chmod`
- Executed the file from the terminal

### Key Learning:
In Linux endpoints, bash spawning `wget`, `chmod`, and executing a file represents the same malicious pattern as PowerShell in Windows.

---

## EDR Mapping Understanding

Through this practice, I understood that EDR focuses on:

- Process tree (parent-child relation)
- Command-line activity
- Download → execute behavior
- Timeline of events

This helped me understand how tools like CrowdStrike and Microsoft Defender present such activity inside their consoles.

---

## Conclusion

This hands-on practice helped me understand EDR investigation mindset without using the actual tool, by generating and analyzing suspicious behavior directly on the system.