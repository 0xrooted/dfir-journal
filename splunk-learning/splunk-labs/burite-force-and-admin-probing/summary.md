# Brute Force Login and Admin Panel Probing Detection

In this part of the analysis, I focused on login activity and attempts to access administrative panels.

By filtering POST requests to the `/login` endpoint, I identified an IP address that generated multiple failed login attempts (HTTP 401), followed by a successful login (HTTP 200). This pattern is a classic sign of a brute-force attack that eventually succeeded.

Additionally, repeated access attempts to `/admin` and related paths resulting in HTTP 403 responses indicated probing of restricted areas of the application.

These findings were derived using targeted SPL queries that filtered logs based on method, URI, and status codes.

This reflects real SOC investigation techniques where analysts correlate failed and successful attempts to detect compromised access.