'''
	Filename: welcome.py
	Author: Sundar P
	Created On: 10 Jan 2017	
	Description: This is sample file
'''
print('Welcome to Python') #print is used display the given values
a=2
b=3
c=(a+b)
print(c,' (+) is used sum the given values') #+ is used sum the given values
namelist = ["Sam", "Peter", "James", "Julian", "Ann"]
print(namelist, ' array of names')
namelist.reverse()
print(namelist, ' array reverse')
namelist.sort()
print(namelist, ' array sort')
print('array count ',len(namelist))

#listone = {1,2,3}
#listtwo = {3,4,5}
#listthree = {'david':1410,'brad':1137}
#print(list(listthree.items()))
#print(listthree.get('sun'))