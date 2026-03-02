seta = set(map(int, input().split()))  
n = int(input())
for i in range(n):
    setb = set(map(int, input().split()))

    if not seta.issuperset(setb):
        print(False)
        break
else: 
    print(True)