n = int(input())
unique = set()
for i in range (n):
    s = input().strip()
    unique.add(s)  
count =0  
for i in unique:
    count +=1
print(count)