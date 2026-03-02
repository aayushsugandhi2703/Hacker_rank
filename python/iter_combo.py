# this program defines a function that takes a string and an integer as input
# and returns a list of all possible combinations of the string of length n
# the function uses the itertools module to generate the combinations
from itertools import combinations

s,n = input().split()
n = int(n)
s = sorted(s)
for j in range(1,n+1):
    for i in combinations(s,j):
        print("".join(i))