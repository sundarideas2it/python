"""	Filename: welcome.py
	Author: Sundar P
	Created On: 10 Jan 2017	
	Description: This is sample file to check random syntax
"""
print('Welcome to Python') #print is used display the given values
a, b='First', 'Name'
print((a+b),' (+) is used concate the given strings') #+ is use to concate the given strings
a, b=2, 3
print((a+b),' (+) is used sum the given values') #+ is use to sum the given values
namelist = ["Sam", "Peter", "James", "Julian", "Ann"]
print(namelist, ' array of names')
namelist.reverse()
print(namelist, ' array reverse')
namelist.sort()
print(namelist, ' array sort')
print('array count ',len(namelist))

listone = {1,2,3}
listtwo = {3,4,5}
listthree = {'Test1':1001,'Test2':2010}
print(list(listthree.items()))
print(listthree.get('Test1'))