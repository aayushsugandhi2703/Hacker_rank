n = int(input())  
nums = set(map(int, input().split()))  

op = int(input())  
commands = [input().split() for _ in range(op)]  

for cmd in commands:
    if cmd[0] == 'pop':
        nums.pop() 
    elif cmd[0] == 'remove':
        nums.remove(int(cmd[1]))  
    elif cmd[0] == 'discard':
        nums.discard(int(cmd[1]))  

print(sum(nums))  
