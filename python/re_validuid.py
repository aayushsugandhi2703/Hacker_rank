import re
pattern = r'(?=(?:.*[A-Z]){2,})(?=(?:.*[0-9]){3,})[a-zA-Z0-9]{10}'
n = int(input())
list =[]
for _ in range(n):
    uid = input()
    list.append(uid)
for i in list:
    if len(i) == 10 and len(set(i)) == 10:
        matches = re.match(pattern, i)
        if matches:
            print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')
        
        