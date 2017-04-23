# usr/bin/env/python3

# Kevin Landau
# 04/23/2017

import sys

file1 = sys.argv[1] # Recall that argv[0] is this script itself.

# The line below allows the file to be opened and read every line into an element of a list. Keep in mind, when opening
# files using .readlines(), you don't need to close the file at the end. This is because it reads the entire file into
# a list, not into memory.
my_tsv_file = open(file1, 'r').readlines() # tsv stands for tab-separated values.


header = my_tsv_file[0] # If your file has a header, it will be the first (zeroth) element in that list.

important_data_lst = [] # Create an empty list to append to later on.

for entry in my_tsv_file[1:]: # This will start iterating through every element beginning from the second position in the list.

    parse1 = entry.rstrip('\n').split('\t') # This removes all end-of-line characters from every element and splits each entire element at any tab characters ('\t').

    datapoint1 = parse1[3] # This is just an example of how you can extract very specific information depending on its position in each line.

    important_data_lst.append(datapoint1) # This appends all desired datapoints into its own, separate list.






