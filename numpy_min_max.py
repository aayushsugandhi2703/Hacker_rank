# This Uses a function of numpy Min and Max to find the minimum and maximum numbers in a numpy array.
# For Min:
# print numpy.min(my_array, axis = 0)         #Output : [1 0]
#print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
#print numpy.min(my_array, axis = None)      #Output : 0
#print numpy.min(my_array)                   #Output : 0

# for Max:
# print numpy.max(my_array, axis = 0)         #Output : [4 7]
#print numpy.max(my_array, axis = 1)         #Output : [5 7 3 4]
#print numpy.max(my_array, axis = None)      #Output : 7
#print numpy.max(my_array)                   #Output : 7

# # # Task
# # You are given a 2-D array with dimensions N X M.
# # Your task is to perform the min function over axis 1 and then find the max of that.

import numpy

inp = list(map(int, input().split()))
n = inp[0]
m = inp[1]
array1 = []
for _ in range(n):
    array1.append(list(map(int, input().split())))
res = numpy.min(array1, axis = 1)
print(numpy.max(res))