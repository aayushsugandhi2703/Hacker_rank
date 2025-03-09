import numpy 
numpy.set_printoptions(legacy='1.13')

arr = list(map(float, input().split()))
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))