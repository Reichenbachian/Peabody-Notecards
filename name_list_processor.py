"""Processes the name list into a text file format."""

with open("name_list_raw.csv", 'r') as csvfile:
    with open("name_list.dat", 'w') as outfile:
        for line in csvfile:
            processed_line = line.strip().split(' ')
            for word in processed_line:
                outfile.write(word + '\n')
