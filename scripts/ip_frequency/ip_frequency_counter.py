input_file = "../../data/sample.log"
ip_count = {}

with open(input_file, "r") as file:
    for line in file:
        if "IP:" in line:
            ip = line.split("IP:")[1].strip()

            if ip in ip_count:
                ip_count[ip] += 1
            else:
                ip_count[ip] = 1

print("IP Frequency Report:\n")

for ip, count in ip_count.items():
    print(f"{ip} -> {count} times")
