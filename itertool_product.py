# using itertools.product to find the cartesian product of two lists
#to take input as a list, we use map function to take input and split function to split the input into list of Integers

from itertools import product

a = list(map(int,input().split()))
b = list(map(int,input().split()))
result = product(a,b)
print(*result)