"""
	Filename: dictionary.py
	Author: Sundar P
	Created On: 25 Jan 2017	
	Description: examples for dictionary related syntax
"""

dicvar = {'Test1':1001,'Test2':2010}
print(dicvar)
print(list(dicvar.keys()))
print(list(dicvar.values()))
dicvar = ('Test1',1001),('Test2',2010)
print(dicvar)
print(dict(dicvar))

forvar = {x: x**2 for x in (2, 4, 6)}
print(forvar)

dicvar = {'one':1,'two':2,'three':3}
print(dicvar)

for key, value in dicvar.items():
	print ('Key=',key, " Value=",value)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
    print('What is your ',q,'?  It is ',a)    

for f in sorted(questions):
    print(f)

dicvar = {'one':1,'two':2,'three':'3'}
print( 'one' in dicvar)

dicvar = {'one':1,'two':2,'three':'3'}
print(dicvar)
dicvar['three'] = 3
print(dicvar)