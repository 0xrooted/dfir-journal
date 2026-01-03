input_file="../data/sample.log"
output_file= "extracted_ip.log"
with open(input_file, "r") as infile:
    with open(output_file, "w") as outfile:
        for line in infile:
            if "IP:" in line:
                outfile.write(line)
print("Ip Extraction complete")