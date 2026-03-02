import numpy

s = list(map(int, input().split()))

zeros_array = numpy.zeros(s, dtype=int)
ones_array = numpy.ones(s, dtype=int)

print(zeros_array)
print(ones_array)
