"""	Filename: fibonacci.py
	Author: Sundar P
	Created On: 10 Jan 2017	
	Description: Fibonacci sequence
"""
print(__doc__)

n, a, b=10, 0, 1
print('Print Fibonacci sequence upto', n) #print is used display the given values
while(b < n):
	print(b)
	a, b=b, a+b
