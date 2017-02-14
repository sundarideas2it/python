"""	Filename: tuple.py
	Author: Sundar P
	Created On: 13 Feb 2017	
	Description: This is sample file to check tuple syntax - tuple is immutable but it contain mutable obj
"""
othervar = (1,2,3,4)
listvar = ['one','two',3,4]
tuplevar = 'one','two',3,4,othervar

print ('Length of list data '+ str(len(listvar)))
print ('Length of tuple data '+ str(len(tuplevar)))

print ('list data')
print (listvar)
print ('Modified last data from list data')
listvar[3]= 'four'
print (listvar)
print ('tuple data')
print (tuplevar)
print ('Modified last data from tuple data')
tuplevar[3]= 'four'
print (tuplevar)
