# this is a numpy function for sum and prod
# For Sum:
# The sum tool returns the sum of array elements over a given axis.
#print numpy.sum(my_array, axis = 0)         #Output : [4 6]
#print numpy.sum(my_array, axis = 1)         #Output : [3 7]
#print numpy.sum(my_array, axis = None)      #Output : 10
#print numpy.sum(my_array)                   #Output : 10

# fro Prod:
# The prod tool returns the product of array elements over a given axis.
#print numpy.prod(my_array, axis = 0)            #Output : [3 8]
#print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
#print numpy.prod(my_array, axis = None)         #Output : 24
#print numpy.prod(my_array)                      #Output : 24

# Task
# You are given a 2-D array with dimensions N X M.
# Your task is to perform the sum tool over axis 0 and then find the product of that result.
import numpy
inp = list(map(int, input().split()))
n = inp[0]
m = inp[1]
array1 = []
for _ in range(n):
    array1.append(list(map(int, input().split())))
res = numpy.sum(array1, axis = 0)
print(numpy.prod(res))