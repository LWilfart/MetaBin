# Open the file in lecture mode
with open('03_nt', 'r') as f:
    lines = f.readlines()

# Make a list to store extract lines
extracted_lines = []

# Indicator telling 'Are we in the right section'
inside_section = False

# Go through lines of the file
for line in lines:
    line = line.strip()
    
    if line.startswith("Sequences producing significant alignments:"):
        inside_section = True
    elif inside_section and line:
        extracted_lines.append(line)
        inside_section = False

# Writing extract lines in a new file
with open('a_nt.txt', 'w') as new_file:
    for line in extracted_lines:
        new_file.write(line + '\n')
