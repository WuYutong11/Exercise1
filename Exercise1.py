# Define the input and output file names
input_file_name = "file_to_read.txt"
output_file_name = "result.txt"

# Read the input file
with open(input_file_name, "r") as input_file:
    text = input_file.read()

# Count the total occurrences of "terrible"
terrible_count = text.count("terrible")

# Split the text into words
words = text.split()

# Initialize a variable to keep track of the occurrence count
occurrence_count = 0

# Replace even occurrences of "terrible" with "pathetic" and odd occurrences with "marvellous"
for i in range(len(words)):
    if words[i] == "terrible":
        occurrence_count += 1
        if occurrence_count % 2 == 0:
            words[i] = "pathetic"
        else:
            words[i] = "marvellous"

# Join the words back into a single text
new_text = " ".join(words)

# Write the new text to the output file
with open(output_file_name, "w") as output_file:
    output_file.write(new_text)

# Print the total count of "terrible"
print(f"Total occurrences of 'terrible': {terrible_count}")

