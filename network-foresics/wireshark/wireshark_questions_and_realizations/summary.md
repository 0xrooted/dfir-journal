# Lesson 3 – Wireshark Questions & Realizations

While working with Wireshark and basic traffic analysis, I had a few doubts.  
These notes are my own understanding after observing real traffic instead of just theory.

---

## Is traffic from a “safe website” always safe?

Initially I thought that if I am visiting well-known websites and traffic is going through port 80 or 443, then it must be safe.

That assumption is not completely correct.

Port 80 and 443 are just commonly used web ports. Even on HTTPS (443), a lot of things can still go wrong, like:
- Background connections without user interaction
- Data being sent out silently
- Malware communicating with its server
- Malicious scripts being loaded from trusted-looking sites

Encryption only hides the content, not the intention behind the traffic.

---

## Can something suspicious really happen on port 443?

Yes, and this was an important realization.

Some red flags I learned to watch for:
- Same domain or IP being contacted repeatedly
- Random or weird-looking domain names
- Traffic continuing even when the browser is closed
- Connections happening at unusual times
- Certificates that don’t properly match the domain

So HTTPS doesn’t automatically mean “safe”.

---

## Do I need to memorize all network protocols?

At first, this felt overwhelming.

But instead of memorizing everything, it makes more sense to understand how a few core protocols behave:
- DNS for name resolution
- TCP for reliable communication
- UDP for fast but unreliable data transfer
- HTTP for plain web traffic
- HTTPS/TLS for encrypted traffic
- ICMP for basic network checks

Other protocols can be learned when they show up in real cases.

---

## How do I decide what traffic is expected and what is not?

This part is not about rules, it’s about context.

A simple way to think about it:
- If traffic happens because I did something (opened a browser, clicked a link), it’s expected.
- If traffic keeps happening without any user action, it needs attention.

One good question to ask is:
“If I stop using the system, should this traffic still exist?”

If the answer is no and traffic still continues, that’s worth investigating.

---

## My DFIR mindset takeaway

Instead of panicking over encrypted traffic, I now try to think in terms of behavior.

For any traffic, I ask:
- Who is talking?
- Where is it going?
- When is it happening?
- Why is it happening?

If I can’t clearly explain the “why”, that’s where DFIR work starts.

---

## Summary

- HTTPS does not automatically mean safe
- Encrypted traffic is normal on modern networks
- Context matters more than protocol names
- DFIR is about observing patterns, not guessing
