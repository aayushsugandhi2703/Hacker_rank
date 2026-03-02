import numpy

s= input().strip().split(' ')
arr = numpy.array(s, int)
arrs = numpy.reshape(arr, (3,3)) 
print(arrs)
'''
shape

The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array.

Reshape

The reshape tool gives a new shape to an array without changing its data. It creates a new array and does not modify the original array itself.

'''