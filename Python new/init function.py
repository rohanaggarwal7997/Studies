class Tuna:
    def __init__(self,x):
        print('I am class Tuna')
        self.energy=x                   #class will have a variable energy

    def swim2(self):
        print(self.energynew)
    def swim(self):
        print('I am swimming with energy',self.energy)
        self.energynew=5
flipper=Tuna(12)
flipper.swim2()
flipper.swim()          #wiil declare error but if you run otherwise then nothing
                        #will work even if you declare new function below