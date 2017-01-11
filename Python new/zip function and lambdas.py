first=['rohan','nikit','anup']
second=['agg','beg','agg']

names=zip(first,second)

for a,b in names:
    print(a,b)

# a lambda function with input x and output x*7

answer = lambda x:x*7

print(answer(7))
