import numpy
numpy.set_printoptions(legacy='1.13')

def func(k):    
    return numpy.eye(k[0], k[1])

s = list(map(int, input().split()))
result = func(s)

print(result)
