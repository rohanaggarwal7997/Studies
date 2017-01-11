stocks={
    'GOOG':520.52,
    'FB':76.45,
    'YHOO':39.28,
    'Aman':99.76
}

# you cannot sort a dictionary but you can sort a list

print(min(zip(stocks.values(),stocks.keys())))
print(max(zip(stocks.values(),stocks.keys())))
print(sorted(zip(stocks.values(),stocks.keys())))

#for one more sorting look at counting words on a page