import sys
import csv
from os.path import dirname

new_rows = []
#changes will search within strings
#need to be add regex to ensure beginning and end

#Need to add input validation for number of arguments
#Need to add input validation for filetype
filename = str(sys.argv[1])
original_dir = dirname(filename)
modfile = original_dir + '/modified.csv'
changes = {
	str(sys.argv[2]) : str(sys.argv[3]),
	}
print "Working with file: ", filename
print "Path is: ", original_dir
print "New file is: ", modfile

with open (filename, 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		new_row = row
		for key, value in changes.items():
			new_row = [ x.replace(key, value) for x in new_row ]
		new_rows.append(new_row)

#possible to open same file, but I want to keep original intact
with open(modfile, 'wb') as f:
	writer = csv.writer(f,)
	writer.writerows(new_rows)
