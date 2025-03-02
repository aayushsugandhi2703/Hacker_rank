import re
n = int(input())
list =[]
for i in range(n):
    s= input().strip()
    list.append(s)
for i in list:  
    patttern  = r"^[789]\d{9}$"
    result = re.match(patttern, i)
    if result:
        print("YES")
    else:
        print("NO")
