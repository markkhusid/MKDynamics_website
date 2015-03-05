#!/usr/bin/python3
import sys
import csv
import os

# Assign constants for better code readability
first_arg = 1
second_arg = 2

# Call the system to get the command line arguments and pull out items from the list
input_file = sys.argv[first_arg]
intermediate_file = 'intermediate.dat'
output_file = sys.argv[second_arg]

# Simple string manipulation that traverses text file until EOF 
# and calls method to replace commas with newline characters
with open(input_file) as infile, open(intermediate_file, "w") as outfile:
  for line in infile:
      outfile.write(line.replace(",", "\n"))

# Close the input file, as it is no longer needed.
infile.close()
      
# Now go through the intermediate file (the file that contains one data element per line)
# and reformat all of the data elements into fixed floating point with 20 decimal precision.
with open(intermediate_file) as infile, open(output_file, "w") as outfile:
  for line in infile:
      outfile.write('%20.20f\n' % float(line))
            
# Close the intermediate file and final output file.
infile.close()
outfile.close()

# Clean away the intermediate file.  The next line may be commented out if the intermediate 
# file is required.
os.remove(intermediate_file)


