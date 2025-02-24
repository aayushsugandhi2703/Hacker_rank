# this problem takes the number of order and its price and we need to find the total order
from collections import OrderedDict

n = int(input())
dict = OrderedDict()
for i in range(n):
    item,price = input().rsplit(' ', 1)
    if item in dict:
        dict[item] += int(price)
    else:
        dict[item] = int(price)
for item, price in dict.items():        
    print(item, price)