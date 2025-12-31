import re
input_file = "../../data/sample.log"
output_file = "timeline.log"
timestamp_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        timestamp = re.search(timestamp_pattern, line)
        if timestamp:
            outfile.write(f"{timestamp.group()} {line}")
print("Timeline Extraction Completed.")