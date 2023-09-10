import subprocess

# Define the modified grep command as a list of strings
grep_command = [
    "grep",
    "-o",
    '"\/[^"]*"',
    "E-Services API.json"  # Replace with your input file name
]

# Run the grep command and capture the output
try:
    result = subprocess.run(grep_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    output = result.stdout
except subprocess.CalledProcessError as e:
    print("Error running grep command:", e)
    output = ""

# Filter out lines that contain "{", and remove double quotes
filtered_output = "\n".join(line.strip('"') for line in output.split("\n") if "{" not in line)

# Define the output file name
output_file = "output.txt"

# Save the filtered grep results to a file
with open(output_file, "w") as file:
    file.write(filtered_output)

print("Results saved to", output_file)
