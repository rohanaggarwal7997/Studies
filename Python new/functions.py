
def gender(sex='m',pr='nothing'):      #u is default value
    if sex is 'm':
        a=3                 #this is a local variable
        print(a)
        print(pr)
        return 'male'
    else:
        a=6                 #if you dont give this then problem as a has been now a local
        print(a)            #so it wont reference to a the global one
        return 'female'     #if you have to use it inside just type global a
a=5
print(gender(pr='hi',sex='m'))
print(gender('a'))
print(gender())
print(a)