# Write a Python program that accepts two integers as input: a and b.Implement the following five functions using proper exception handling and logging:
# 1. Prime Numbers Between a and b
# Function Name: find_primes(a, b)
# Find and return all prime numbers between a and b. Swap if a > b.
# 2. Fibonacci Series of Length b
# Function Name: fibonacci_series(length)
# Print the first b numbers in the Fibonacci series. If b is negative or zero, raise an appropriate exception.
# 3. Sum of Digits of a and b
# Function Name: sum_of_digits(n)
# Return the sum of digits of both a and b.
# 4. Factorial of a and b
# Function Name: calculate_factorial(n)
# Compute the factorial of a and b. If either number is negative, raise an error.
# 5. Count Even and Odd Numbers Between a and b
# Function Name: count_even_odd(a, b)
# Return the count of even and odd numbers in the range from a to b.


# Write a Python function to flatten a nested list.
# flatten([1, [2, [3, 4], 5], 6]) o/p: [1, 2, 3, 4, 5, 6]

def flatten(nested_list):
    flattened_list = []
    for i in nested_list:
        if type(i) == list:
            flattened_list += flatten(i)
        else:
            flattened_list.append(i) 
    return flattened_list

print(flatten([1,[2,[3,4],5],6]))

# Write a Python function to check if a string has balanced parentheses, brackets, and braces.
# is_balanced("({[]})") o/p: True
# is_balanced("([)]")   o/p: False
# is_balanced("{[()]}") o/p: True
# is_balanced("{[(])}") o/p: False

def is_balanced(str1):
    stack = []
    for i in str1:
        if i in ("[","{","("):
            stack.append(i)
        elif i in ("]","}",")"):
            if not stack:
                return False
            top = stack.pop()
            if (i == "}" and top != "{") or (i == ")" and top != "(") or (i == "]" and top != "["):
                return False
    return not stack

print(is_balanced("({[]})"))
print(is_balanced("([)]"))
print(is_balanced("{[()]}"))
print(is_balanced("{[(])}"))
        
# How do you count the occurrences of each element in a list using a dictionary?

list1 = ['apple','banana','kiwi','apple','orange','apple']
count = {}
for i in list1:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)

# Define a function do_nothing that does nothing when called. This function should be syntactically correct.

def do_nothing():
    pass

do_nothing()

# invert a dictionary
# d = {'a': 1, 'b': 2, 'c': 3}

d = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = {value:key for key,value in d.items()}
print(inverted_dict)

# How do you create a dictionary using a dictionary comprehension that maps numbers to their squares for numbers 1 through 5?

squares = {x:x**2 for x in range(1,6)}
print(squares)

# Write a Python function that accepts an arbitrary number of integers as input and returns their sum.
# sum_all(1, 2, 3) o/p: 6
# sum_all(5, 10, 15, 20) o/p: 50
# sum_all() o/p: 0

def sum_all(*num):
    return sum(num)

print(sum_all(1,2,3))
print(sum_all(5, 10, 15, 20))
print(sum_all())   

# Write a function greet_user that takes one required argument name, and two optional keyword arguments greeting (default: "Hello") and punctuation (default: "!").
# greet_user("Alice") o/p: "Hello, Alice!"
# greet_user("Bob", greeting="Hi") o/p: "Hi, Bob!"
# greet_user("Eve", punctuation=".") o/p: "Hello, Eve."
# greet_user("Sam", greeting="Good morning", punctuation="!") o/p: "Good morning, Sam!"

def greet_user(name,greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

print(greet_user("Alice"))
print(greet_user("Bob",greeting="Hi"))
print(greet_user("Eve",punctuation="."))
print(greet_user("Sam",greeting="Good morning",punctuation="!"))