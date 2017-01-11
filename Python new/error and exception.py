#tuna=int(input('What\'s your fav no\n'))#now if you enter a string as input thats an exception
while True:
    try:
        num=int(input('What\'s your fav no\n'))
        print(18/num)
        break
    except ValueError:
        print('Make Sure you Ener a number')
    except ZeroDivisionError:
        print('Don\'t Pick Number')
    except:                     #for default exception
        break
    finally:                    #no matter what execute this
        print('Loop complete')