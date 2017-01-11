class Parent:
    def printlastname(self):
        print('Aggarwal')
class Child(Parent):            #inherited Parent class
    def print_name(self):
        print('Rohan')

    def printlastname(self):        #overwriting parent function
        print('Aggar')

bucky=Child()
bucky.print_name()
bucky.printlastname()