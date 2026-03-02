from collections import deque

d = deque()  

n = int(input())  

for _ in range(n):  
    command = input().split()  

    if command[0] == "pop":
        if d:  
            d.pop()
    elif command[0] == "popleft":
        if d:
            d.popleft()
    elif command[0] == "append":
        d.append(int(command[1]))  
    elif command[0] == "appendleft":
        d.appendleft(int(command[1]))

print(" ".join(map(str, d)))
