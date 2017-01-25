"""
	Filename: truthvalue.py
	Author: Sundar P
	Created On: 25 Jan 2017	
	Description: examples for truth value testing
"""
def my_function(a,b):
	print (not a == b)
	print (a == b or a < b)
	print (a == b and a < b)

my_function(5,6)

def my_function(a,b):
	print (round(a))
	print (round(b))	

my_function(5.15,6.60)