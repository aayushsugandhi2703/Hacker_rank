import numpy as np

n = int(input())  

a = [list(map(int, input().split())) for _ in range(n)]
a = np.array(a)

b = [list(map(int, input().split())) for _ in range(n)]
b = np.array(b)

result = np.dot(a, b)

print(result)
