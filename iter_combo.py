from itertools import combinations

s,n = input().split()
n = int(n)
s = sorted(s)
for j in range(1,n+1):
    for i in combinations(s,j):
        print("".join(i))