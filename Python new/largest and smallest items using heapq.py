import heapq

grades=[34,324,234,123,3242,3421,12]
print(heapq.nlargest(3,grades))

stocks=[
    {'ticker':'appl','price':'201'},
{'ticker':'go','price':'2301'},
{'ticker':'f','price':'2021'},
{'ticker':'tuna','price':'2011'}
]
print(heapq.nsmallest(2,stocks,key=lambda stock:stock['price']))