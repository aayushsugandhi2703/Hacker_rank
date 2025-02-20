from cmath import phase

def fun(real, imaginary):
    print(abs(complex(real, imaginary)))
    print(phase(complex(real, imaginary)))

str = input()
str = str.split('+')
real = int(str[0])
imaginary = int(str[1][:-1])
fun(real, imaginary)

# Output:
# 1+2j
# 2.23606797749979
# 1.1071487177940904