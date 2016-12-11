import random
import sys
import os
'''
for x in range(0,10):	#end at 9
  print(x,' ',end="")
lis=['a','b','c','d']
for y in lis:  #browse through entire list
  print (y)
num_list=[[1,2,3],[10,20,30],[4,5,6]]	#create list of lists
for x in range(0,3):		
  for y in num_list[x]:#do same indentation at each place
    print(y)		#browse through list
for x in range(0,3):
  for y in range(0,len(num_list[x])):
    print(num_list[x][y])

random_num =random.randrange(0,100) #to get a random number
while(random_num!=15):
	print(random_num)
	random_num=random.randrange(0,100)

i=0;
while(i<=20):
	if(i%2==0):
		print(i)
	elif(i==9):
		break	#same as c++
	else:
		i+=1
		continue  #same as c++
	i+=1		
...
