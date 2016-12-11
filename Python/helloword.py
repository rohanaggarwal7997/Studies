import random
import sys
import os
print("Hello World Fuck You")
#can be inside single or double quotes
#separate different things with a comma
#Every print statement is in different line otherwise include at end -> ,end=""
#print 5 new lines print("\n"*5)
name="Derek"
#Variable has to start with letter and then it can have numbers and underscores
#5 main data types Numbers Strings Lists Tuples Dictionaries
#7 Different algorithmic operations + - * / % **- exponential //Floor division
print(5+2," \n",5-2," ",5*2," ",5/2," ",5%2," ",5**2," ",5//2)
#multiplicatiopn and division order is > addition and subtraction
print(5-2*3)
print(name)
#print(name%2)
name=5
print(name%2)
#campp
'''
ashfabuwiorfhawl
'''
#You have to escape a " if you want to print it inside a string
quote="\"Always remember you are unique"
print(quote)
#What about"'"? That also works 
quote="'Always remember you are unique"
print(quote)
#Multi line strings
Multi_line='''Rohan is 
The best'''
#Joining two strings
join=Multi_line+quote
print(join)
print("%s %s %s "%("Rohan is the best",quote,Multi_line))
# passing arguments in the print function in the string Still not clear why we have to pass varia
#bles in %()->Check that

