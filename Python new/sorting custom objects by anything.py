from operator import attrgetter

class User:
    def __init__(self,x,y):
        self.name=x
        self.user_id=y

    def __repr__(self):         #string representation of the objext
        return self.name+":"+str(self.user_id)


users=[
    User('Rohan',43),
User('Shivram',13),
User('Shivam',23),
User('Roopansh',33),
User('Shubham',45),
User('Ankit',53),
User('Harshit',63)
]

for user in users:
    print(user)


print('--------------')

for user in sorted(users,key=attrgetter('name')):
    print(user)
