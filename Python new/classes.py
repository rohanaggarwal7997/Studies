class Enemy:
    life=3
    def attack(self):
        print('Ouch!')
        self.life-=1
    def checklife(self):
        if self.life<=0:
            print('I am dead')
        else:
            print('Not dead')

enemy1=Enemy()
enemy1.attack()
enemy1.checklife()