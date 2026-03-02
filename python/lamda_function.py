''''
'What are lambda functions in Python?
A lambda function in Python is an anonymous (nameless) function. It's a way to create a small, simple function in a single line, without formally defining it using def.

Basic Syntax:

lambda arguments: expression
lambda is the keyword.
You can have any number of arguments, but only one expression.
The result of the expression is returned automatically.
Example 1:

# Normal function
def add(x, y):
    return x + y

# Equivalent lambda function
add_lambda = lambda x, y: x + y

print(add_lambda(5, 3))  # Output: 8
Example 2: Lambda with no arguments:

greet = lambda : "Hello!"
print(greet())  # Output: Hello!
Where is it useful?
Lambda functions are mostly used when you need a quick function for short-term use, especially as an argument to higher-order functions like map(), filter(), and sorted().

Example 3: Lambda inside map()

nums = [1, 2, 3, 4, 5]

# Double each number
doubled = list(map(lambda x: x * 2, nums))

print(doubled)  # Output: [2, 4, 6, 8, 10]
Example 4: Lambda with sorted()

# Sort a list of tuples by the second value
pairs = [(1, 4), (2, 1), (3, 3)]

sorted_pairs = sorted(pairs, key=lambda x: x[1])

print(sorted_pairs)  # Output: [(2, 1), (3, 3), (1, 4)]
Limitations of lambda:
It's meant for simple functions.
You can only have one expression, no statements (like loops or multiple lines).
For complex logic, it's better to use def.'
'''
# Lambda function to calculate the cube of a given number
cube = lambda x: x ** 3

# Function to generate the Fibonacci sequence up to n terms
def fibonacci(n):
    lists = []  # Initialize an empty list to store Fibonacci numbers
    a = 0       # First Fibonacci number
    b = 1       # Second Fibonacci number
    
    # Loop to generate n Fibonacci numbers
    for i in range(n):
        lists.append(a)    # Append the current number to the list
        a, b = b, a + b    # Update a and b to the next two numbers in the sequence
        
    return lists  # Return the list of Fibonacci numbers

# The starting point of the program
if __name__ == '__main__':
    n = int(input("Enter the number of terms: "))  # Take user input for how many terms of Fibonacci to generate
    
    # Generate Fibonacci numbers and apply the cube lambda function to each one
    result = list(map(cube, fibonacci(n)))
    
    # Print the final list of cubes of the Fibonacci numbers
    print(result)
