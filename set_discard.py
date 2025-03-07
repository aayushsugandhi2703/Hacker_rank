n = int(input())  
nums = set(map(int, input().split()))  

op = int(input())  
commands = [input().split() for _ in range(op)]  

for cmd in commands:
    if cmd[0] == 'pop':
        if nums:  # Check if set is non-empty before popping
            nums.remove(min(nums))
    elif cmd[0] == 'remove':
        if int(cmd[1]) in nums:  # Check before removing to avoid KeyError
            nums.remove(int(cmd[1]))  
    elif cmd[0] == 'discard':
        nums.discard(int(cmd[1]))  # Safe, no KeyError raised

print(sum(nums))  
