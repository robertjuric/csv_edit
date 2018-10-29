import sys
import csv
import os.path
from os.path import dirname
import re

#Some Variables
original_file = str(sys.argv[1])
original_dir = dirname(original_file)
mod_file = original_dir + '/modified.csv'
changes = {
	str(sys.argv[2]) : str(sys.argv[3]),
	}
new_rows = []

#Input validation for number of arguments
if len(sys.argv) < 4:
	print "Incorrect syntax."
	print "Correct syntax: replace.py file.csv search_string replace_string"
	sys.exit(2)
#Input validation for the file
#Regex search for ends with '.csv'
p = re.compile('\.csv\Z')
m = p.search(original_file)
if m:
	#File ends in .csv
	#Check if file actually exists
	if not os.path.exists(original_file):
		print "File submitted does not exist"
		sys.exit()
else:
	print "Filename submitted is not a CSV file"
	sys.exit()

#Open original file
print "Opening file..."
with open (original_file, 'rb') as f:
	reader = csv.reader(f)
	#Loop through each row
	for row in reader:
		new_row = row
		#Search and replace values
		for key, value in changes.items():
			new_row = [ x.replace(key, value) for x in new_row ]
		#Write new values into array
		new_rows.append(new_row)

#Open new modified file
#Possible to open same file, but I want to keep original intact
print "Writing new file..."
with open(mod_file, 'wb') as f:
	writer = csv.writer(f,)
	#Write new_rows array into file
	writer.writerows(new_rows)
print "Complete."