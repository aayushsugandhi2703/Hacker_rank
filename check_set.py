t = int(input())

for _ in range(t):
    n = int(input())  
    A = set(map(int, input().split()))  
    m = int(input())  
    B = set(map(int, input().split())) 
    print(A.issubset(B))
