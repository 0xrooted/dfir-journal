username = input("Enter the Username: ")
input_file = "../../data/sample.log"
output_file= f"user_{username}_logs.log"

found = False

with open (input_file,"r") as infile:
    with open(output_file,"w") as outfile:
        for line in infile:
            if f"user={username}" in line:
                outfile.write(line)

found = True

if found:
    print(f"Logs saved for user: {username}")
else:
    print("User didn't exist")