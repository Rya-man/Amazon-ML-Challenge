import csv

# File paths (input and output files)
input_file = 'result.csv'
output_file = 'output.csv'

# Open the input CSV for reading and the output CSV for writing
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Copy the original data into the output file
    for row in reader:
        writer.writerow(row)

    # Append lines from 2758 to 131287
    for i in range(2758, 131288):
        writer.writerow([i, ''])

print(f"Appended lines from 2758 to 131287 to {output_file}.")

