income=[10,11,12]

def double_money(dollars):
    return dollars*2

print(map(double_money,income))         #important map object see below
new_income=list(map(double_money,income))
print(new_income)