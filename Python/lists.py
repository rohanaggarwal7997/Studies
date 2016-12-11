#include random
#include sys
#include os

grocery_list=['Juice','Tomatoes',1,2,3]
print(grocery_list[1],grocery_list[3])
grocery_list[1]='Rohan'
print(grocery_list[1],grocery_list[3])
print(grocery_list[1:4])#Does not print the 4th
st=grocery_list[1:4]#can be stored in a string also
print(st)

#list of lists
newlist=[grocery_list,'Rohan']
print(newlist[0][1],newlist[1])
print(newlist[0],newlist[1])#This prints the entire list
#print(newlist[2]) error
#newlist[2]='rohan' error
newlist.append('Rohan')
print(newlist[2])


#Operations on lists
list1=grocery_list
list1.insert(1,'Piyush') #inserts at starting
print(list1)
list1.remove('Rohan') #removes only one instance
#list1.sort() #problem as can't order between string and integer
list1.reverse()
del list1[3]
print(list1)
todo=grocery_list+list1
print(len(todo))
#print(max(todo)) will print errors due to integers in list
#print(min(todo))
todo.remove(1)
todo.remove(2)
todo.remove(3)
todo.remove(1)
todo.remove(2)
todo.remove(3)
print(max(todo))
print(min(todo))



#TUPLES
#cant change them 
newtuple=(1,2,3,4,5)
#Interconverting list to a tuple
lis=list(newtuple)
tupl=tuple(lis)
lis.remove(1)
#tupl.remove(1) error
print(lis)
print(tupl)
#tuple functions 
#len(tuple) min(tuple) max(tuple)

