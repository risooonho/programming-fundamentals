## Sorting Fruits

#Open files for input and output
infile = open("unsorted_fruits.txt", "r")
outfile=open("sorted_fruits.txt","w")

# Creates empty list for receiving the fruit words from input file
list_of_fruits = []

# Read every line in file
for line in infile:
    # Read every word in line (ignoring white spaces)
    for word in line.split():
        # Append word to list
        list_of_fruits.append(word)


# Create new list with sorted words
sorted_list_of_fruits = sorted(list_of_fruits)

# Write sorted words in output file
for fruit in sorted_list_of_fruits:
    outfile.write(fruit+"\n")

# Close files
infile.close()
outfile.close()


