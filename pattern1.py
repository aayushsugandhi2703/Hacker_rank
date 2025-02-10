#pattern
# 1
# 22
# 333
# 4444
n = int(input())  

for i in range(1, n):  # Loop from 1 to n-1
    print(str(i) * i)  # Print i repeated i times


# another way to do this is:

for i in range(1,n):
    sum =0
    for j in range(i):
        sum =(sum *10) +i
    print(sum)