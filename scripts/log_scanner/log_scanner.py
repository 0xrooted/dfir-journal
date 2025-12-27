keywords = ["failed", "error", "denied"]
input_file= "../../data/sample.log"
output_file= "suspecious.log"
with open(input_file,"r") as infile:
    with open(output_file,"w") as outfile:
        for line in infile:
            for word in keywords:
                if word in line.lower():
                    outfile.write(line)
                    break
print("Scan Completed! Suspecious logs saved.")