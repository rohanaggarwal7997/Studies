import random
import sys
import os
#u cant combine dictionaries
dicti={ 'a':1,'b':2,
	'c':3,'d':4,
	'e':5
	}
print(dicti['a'])
del dicti['a']
dicti['b']=10
print(len(dicti))
print(dicti.get('a'))#no error
#print(dicti['a'])#generates error
print(dicti.keys())
print(dicti.values())
