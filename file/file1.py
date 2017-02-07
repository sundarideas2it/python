"""	Filename: file1.py
	Author: Sundar P
	Created On: 07 Feb 2017	
	Description: This is sample file to read text from file
"""

sf = open('singlelinefile.txt','r')
for line in sf:
    print(line, end='')
sf.closed
