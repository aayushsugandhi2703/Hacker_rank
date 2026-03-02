# this program use itertools to generate all possible combinations of a string
# it uses combinations_with_replacement instead of combinations
# this allows for repeated elements in the combinations

from itertools import combinations_with_replacement

s,n = input().split()
n = int(n)
s = sorted(s)
for i in combinations_with_replacement(s,n):
    print("".join(i))