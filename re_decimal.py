import re

pattern = r"[+-]?\d*\.\d+"
n = int(input())
lst = []
for i in range(n):
    no = input().strip()
    lst.append(no)
for i in lst:
    if re.fullmatch(pattern,i):
        print(True)
    else:
        print(False)