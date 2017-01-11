name='rohan aggarwal'
if name is 'rohan':
    print('You are great')
elif name is 'rohan aggarwal':
    print('You are also great')
else:
    print('You might be great')

numb=[1,2,3,4,5]

for f in numb[:2]:
    print(f)
    print('\n')

#:2 is very important


#range --very important
for x in range(5,12):      #means 0to 10 if only 1 number start from 0
    print('x is right now',x)
for x in range(6,12,2):
    print('y is right now',x)
    if x==8:
        continue
z=1
while z<10:
    print('z is right now',z)
    z+=1
    if z==5:
        break

'''

Long range comment

'''

# checking if a number is in a list if n in list_name