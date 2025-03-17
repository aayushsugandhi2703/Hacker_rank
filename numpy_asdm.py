import numpy as np

# Read n and m
n, m = map(int, input().split())

# Read first array
array1 = []
for _ in range(n):
    array1.append(list(map(int, input().split())))

# Read second array
array2 = []
for _ in range(n):
    array2.append(list(map(int, input().split())))

# Convert to numpy arrays
a = np.array(array1)
b = np.array(array2)

# Perform operations
print(a + b)                    
print(a - b)                    
print(a * b)                    
print(a // b)                   
print(a % b)
print(a ** b)                   
