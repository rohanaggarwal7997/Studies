stocks={
   'igi':3453,
    'AAP':3433,
'FB':3443,
'SFI':3243,
}
min_price=min(zip(stocks.values(),stocks.keys()))   #sorts according to values
print(min_price)