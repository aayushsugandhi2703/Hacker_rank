# the problem states that we have to find the total amount of money earned by the shopkeeper
# the shopkeeper has a list of shoe sizes and their prices
# the shopkeeper has to sell the shoes to the customers

from collections import Counter

nos = int(input("number of shoes: "))
size = Counter(map(int, input("enter sizes availale").split()))
noc = int(input(" number of customers: "))

total = 0

for i in range(noc):
    shoe_size, price = map(int, input(" enter the size required with its price").split())
    if size[shoe_size]>0:
        total += price
        size[shoe_size] -=1
print(total)
        