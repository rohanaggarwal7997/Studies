date,name,price=['rohan','nikit',8.51]
print(name)
print(price)

def drop_first_last(grades):        #very important
    first,*middle,list=grades
    avg=sum(middle)/len(middle)
    print(avg)

drop_first_last([1,2,3,4,5])