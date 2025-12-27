username = input("Enter the username: ")
input_file = "../../data/sample.log"
username_count = {}

with open(input_file, "r") as file:
    for line in file:
        if f"user={username}" in line:
            user = username  # confirmed user match

            if user in username_count:
                username_count[user] += 1
            else:
                username_count[user] = 1

print("\nUser Activity Report:\n")

if username_count:
    for user, count in username_count.items():
        print(f"{user} -> {count} times")
else:
    print("No activity found for this user.")
