import sys
import csv
import os.path
from os.path import dirname
import re

new_rows = []
#changes will search within strings
#need to be add regex to ensure beginning and end

#Input validation for number of arguments
if len(sys.argv) < 4:
	print "Incorrect syntax"
	print "Correct syntax: replace.py file.csv search_string replace_string"
	sys.exit(2)


original_file = str(sys.argv[1])
print "Working with file: ", original_file
#Regex search for ends with '.csv'
p = re.compile('\.csv\Z')
m = p.search(original_file)
if m:
	#File ends in .csv
	#Check if file actually exists
	if not os.path.exists(original_file):
		print "File does not exist"
		sys.exit()
else:
	print "File listed is not a CSV file"
	sys.exit()

original_dir = dirname(original_file)
print "Path is: ", original_dir

mod_file = original_dir + '/modified.csv'
print "New file is: ", mod_file

changes = {
	str(sys.argv[2]) : str(sys.argv[3]),
	}

with open (original_file, 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		new_row = row
		for key, value in changes.items():
			new_row = [ x.replace(key, value) for x in new_row ]
		new_rows.append(new_row)

#possible to open same file, but I want to keep original intact
with open(mod_file, 'wb') as f:
	writer = csv.writer(f,)
	writer.writerows(new_rows)
