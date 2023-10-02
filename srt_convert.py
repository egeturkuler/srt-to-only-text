import re

# Input and output file paths
input_file_path = 'F:\code-proj\srt-to-only-text\podcast.srt'
output_file_path = 'F:\code-proj\srt-to-only-text\output2.srt'

# Regular expression pattern to match numbers, colons, hyphens, commas, and greater than signs
pattern = re.compile(r'[\d:,->]')

# Function to remove unwanted characters from a line
def remove_unwanted_characters(line):
    return re.sub(pattern, '', line)

# Open the input and output files
with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    in_subtitle = False
    for line in input_file:
        # Check if the line contains the sequence number (indicating a subtitle entry)
        if line.strip().isdigit():
            in_subtitle = True
            output_file.write(line)
        elif in_subtitle:
            # Remove unwanted characters from the line
            modified_line = remove_unwanted_characters(line)
            output_file.write(modified_line)
        else:
            output_file.write(line)
