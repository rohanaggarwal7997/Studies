import threading        #threading is a module Thread is a class

class BuckyMessenger(threading.Thread):
    def run(self):                  #overwrite self function
        for _ in range(1000):         #dont need a variable just wanna loop 10 times
            print(threading.currentThread().getName())

x=BuckyMessenger(name='Send Out Messages')
y=BuckyMessenger(name='Recieve messages')
x.start()       #you dont need to wait for this to finish to move to next line
y.start()


#reference https://www.tutorialspoint.com/python/python_multithreading.htm