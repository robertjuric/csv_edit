import csv


new_rows = []
#changes will search within strings
#need to be add regex to ensure beginning and end
changes = {
	'10.5.42.10' : 'something-changed',
	}

# need to add command line args for csv file and possible replacements

with open ('test1.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		new_row = row
		for key, value in changes.items():
			new_row = [ x.replace(key, value) for x in new_row ]
		new_rows.append(new_row)

#possible to open same file, but I want to keep original in tact
with open('modified.csv', 'wb') as f:
	writer = csv.writer(f,)
	writer.writerows(new_rows)
