import random
import sys
import os
string="rohan is a very good boy"
print(string[0:4])
print(string[-5:])#last 5 characters only -5 5th last character
print(string[:-4])#till the 4th last character
print(string[:4]+"be there")
print("%c is my %s letter and my number %d number is %.5f"%('X','favourite',1,.14))
string=string.capitalize()
print(string)#this is a very important concept
#print(string.capitalize())#only first letter
print(string.find('very'))#make sure that it is according to case sensitivity
print(string.isalpha())#all alphabets
print(string.isalnum())#all numbers
print(len(string))
#print(string.len()) error remember always len(structure)
print(string.replace("very","very very"))
print(string.strip())#strips white spaces
quote_list=string.split(" ")#split according to white spaces
print(quote_list)
