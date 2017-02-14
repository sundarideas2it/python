"""	Filename: readfile.py
	Author: Sundar P
	Created On: 14 Feb 2017	
	Description: This is sample file to work out file concept
"""
# Read a content from file and print the content line by line
filevar = open('emailcontent1.txt','rt')# 'rt' To open a file in read text file mode
for line in filevar:
	print(line,end='')#print the content line by line

filevar = open('emailcontent1.txt','rt')
contents = filevar.read()#read the whole content
filevar.close()
print(contents)#print the whole content

# Read a content from file and append to the variable line by line
lines = []
with open ('emailcontent1.txt', 'rt') as filevar: # This is the another method to read the file
	for line in filevar:
		lines.append(line)
print(lines)#print the file content in list format

# Read file content and open a new or existing file and write content to the file line by line
filevar = open('emailcontent1.txt','rt')
outfile = open('outputcontent.txt','w')# 'rt' To open a file in write mode
for line in filevar:
	outfile.write(line)