# This script takes a dictionary file and trims it to only include words of a certain length.
# The original dictionary used was about 4 MB in size and I wanted something more manageable.
#
# The new dictionary will only include words between 8 and 10 characters in length.  However the
# initial result still managed to be larger than desired.
#
# The final version of the script throws out roughly 50% of the qualified entries and gave me 
# an output file roughly 800KB
from random import randint

dictionary = "rocky.txt"


# Python file operations
# open(file_name, mode) "rt" is default
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)
dictionary = open(dictionary, "r").readlines()
new_dictionary = []


# Checking each word for length, with a coin flip on if the word should be discarded
# Newlines will throw off the length check and will be trimmed first
for word in dictionary:
	word = word.strip('\n')
	if len(word) >= 8 and len(word) <= 10 and randint(0,1) == 1:
		new_dictionary.append(word)

# Creating a new file from new_dictionary
# Newlines have to be added back
newfile = open("trimmed.txt", "w")
for newwords in new_dictionary:
	newfile.writelines(newwords + '\n')

newfile.close()