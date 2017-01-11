# ** for raise to power and // for divide and take zint
print(3 ** 3)
print(4 // 3)

#for strings if you have " ' then include in opposite otherwise do like \ escaping
#\n is for new line
print("Rohan is \" the best")
#r for printing strings in raw
print('\n')
print(r'\n')
#adding strings mean concating
#string name *5 add 5 times
# var='string'  var[-1] is last element
a='rohan'
b=a[2:3]
c=a[2:]
d=a[:5]
print(a+b+c+d)
print(len('This prints the lenght of the string'))


#lists
players=[1,2,3,4,5]
print(players[0],players[1],players)
#adding two lists and changing an element
players=players+[6,7,8]
players[2]=4
print(players)
#appending at end
players.append(8)
print(players)
#slicing elements
print(players[:2])
#replacing multiple elements
players[:2]=[0,0]
print(players)
#removing
players[:2]=[]
print(players)