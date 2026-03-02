import numpy
s = list(map(int, input().split()))
n = s[0]
m = s[1]
array1 = []
for _ in range(n):
    array1.append(list(map(int, input().split())))
me = numpy.mean(array1, axis = 1)
print (me)
va = numpy.var(array1, axis = 0)
print (va)
print (numpy.std(array1))