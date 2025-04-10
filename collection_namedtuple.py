# Basically, namedtuples are easy to create, lightweight object types.
# They turn tuples into convenient containers for simple tasks.
# With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

# The problem is to find the average marks of a student from the given input.
# The input consists of a number of students and their marks.
# The output should be the average marks of the students rounded to two decimal places.

from collections import namedtuple
n = int(input())
total = 0
fields = input().split()
student = namedtuple('student', fields)
for i in range (n):
    data = input().split()
    s = student(*data)
    total+= int(s.MARKS)
print (float("{:.2f}".format(total / n)))