n = input()

lower_case = []
upper_case = []
odd_digits = []
even_digits = []

for i in n:
    if i.islower():
        lower_case.append(i)
    elif i.isupper():
        upper_case.append(i)
    elif i.isdigit() and int(i)%2 != 0:
        odd_digits.append(i)
    elif i.isdigit() and int(i)%2 == 0:
        even_digits.append(i)

lower_case = sorted(lower_case)
upper_case = sorted(upper_case)
odd_digits = sorted(odd_digits)
even_digits = sorted(even_digits)


s = ''
for i in lower_case:
    s = s +i

for i in upper_case:
    s = s +i

for i in odd_digits:
    s = s +i

for i in even_digits:
    s = s +i

print(s)