'''
	Filename: fibonacci.py
	Author: Sundar P
	Created On: 10 Jan 2017	
	Description: Fibonacci sequence
'''
n=10
print('Print Fibonacci sequence upto', n) #print is used display the given values
a=0
b=1
c=(a+b)
print(a)
while(c < 10):
	print(c)
	c=(a+b)	
	a=b
	b=c
print("End")