def add_number(*args):      # this is a tuple
    print(args)
    total=0
    for a in args:
        total+=a

    print(total)


add_number(3+4+7)
add_number(3)

def add(a,b,c):
    print(a+b+c)

list=[1,2,3]
add(*list)                  #unpacking arguments