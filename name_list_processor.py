"""Processes the name list into a text file format."""

with open("name_list_raw.csv", 'r') as csvfile:
    with open("name_list.dat", 'w') as outfile:
        for line in csvfile:
            processed_line = line.strip()
            if processed_line.startswith('"'):
                outfile.write(processed_line.split(',')[0][1:] + '\n')
            else:
                outfile.write(processed_line + '\n')
