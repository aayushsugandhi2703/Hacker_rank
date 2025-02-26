from itertools import combinations

n= int(input())
s = input().split()
k = int(input())

a_index = [i for i in range(n) if s[i]=='a']

combination = list(combinations(range(n),k))

total_a =sum(1 for combo in combination if any (i in a_index for i in combo))

probability = total_a/len(combination)

print(f"{probability:.4f}")
