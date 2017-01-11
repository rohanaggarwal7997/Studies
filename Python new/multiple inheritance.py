class Mario:
    def move(self):
        print('I am moving')
class Shroom:
    def eat_shroom(self):
        print('Now i am big')

class BigMario(Mario,Shroom):
    pass            #want a blank line class needs to have something

bm=BigMario()
bm.move()
bm.eat_shroom()