import math
import os
import random
import re
import sys


def gradingStudents(grades):
    result =[]
    for grade in grades:
        if grade<38:
            result.append(grade)
        else:
            res =  ((grade // 5) + 1) * 5
            if res-grade <3:
                result.append(res)
            else:
                result.append(grade)  
    return result  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
