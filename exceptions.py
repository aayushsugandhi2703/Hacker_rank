# Number of test cases for the input
n = int(input())

for _ in range(n):
    try:
        a, b = input().split()  
        print(int(a) // int(b))  
    except ZeroDivisionError as e:
        print(f"Error Code: {e}")
    except ValueError as e:
        print(f"Error Code: {e}")
