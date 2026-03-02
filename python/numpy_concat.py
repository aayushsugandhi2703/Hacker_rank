import numpy
s = list(map(int, input().split()))
list1 = []
list2 = []
for i in range(s[0]):
    m = input().split()
    list1.append(m)
arr1 = numpy.array(list1, int)
for i in range(s[1]):
    n = input().split()
    list2.append(n)
arr2 = numpy.array(list2, int)
print(numpy.concatenate((arr1, arr2)))