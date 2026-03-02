# This is a solution to the problem of numpy inner and outer problem in the domain of python on the platform of HackerRank.
# Problem Statement: You are given two arrays: A and B. Your task is to compute their inner and outer product.
# Inner Product: The inner product of two arrays is an array of the same dimension, which is calculated by multiplying the elements of the arrays.
# Outer Product: The outer product of two arrays is an array of the shape (A.shape[0], B.shape[0]), where the element 'i' of the array is the product of the elements of the 'i'th element of the first array and all the elements of the second array.

import numpy
arr1 = numpy.array(input().split() , int)
arr2 = numpy.array(input().split() , int)
print(numpy.inner(arr1, arr2))
print(numpy.outer(arr1, arr2))