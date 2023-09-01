def main():
    input_file_name = "file_to_read.txt"
    output_file_name = "result.txt"

    with open(input_file_name, "r") as input_file:
        text = input_file.read()

    # Calculate the total times "terrible" appears
    total_terrible = text.count("terrible")
    print(f"Total occurrences of 'terrible': {total_terrible}")

    # Replace even occurrences with "pathetic" and odd occurrences with "marvellous"
    words = text.split()
    for i in range(len(words)):
        if words[i] == "terrible":
            if i % 2 == 0:
                words[i] = "pathetic"
            else:
                words[i] = "marvellous"

    modified_text = " ".join(words)

    # Write modified text to the output file
    with open(output_file_name, "w") as output_file:
        output_file.write(modified_text)

    print(f"Modified text written to '{output_file_name}'")


if __name__ == "__main__":
    main()
