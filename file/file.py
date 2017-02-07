"""	Filename: file.py
	Author: Sundar P
	Created On: 07 Feb 2017	
	Description: This is sample file to write text to file and read text from file
"""
f = open('singlelinefile.txt','w')
value = ('To write other than string. first convert that into string and then write to file', 999)
s = str(value)
f.write(s)
f.write(' This text is append to the file \n This will print to the next line\n')

fr = open('samplefile.txt','r')
for line in fr:
    print(line, end='')