# Write a Python program that accepts two integers as input: a and b. Implement the following five functions using proper exception handling and logging:
# 1. Prime Numbers Between a and b
# Function Name: find_primes(a, b)
# Find and return all prime numbers between a and b.
# Swap if a > b.
# 2. Fibonacci Series of Length b
# Function Name: fibonacci_series(length)
# Print the first b numbers in the Fibonacci series.
# If b is negative or zero, raise an appropriate exception.
# 3. Sum of Digits of a and b
# Function Name: sum_of_digits(n)
# Return the sum of digits of both a and b.
# 4. Factorial of a and b
# Function Name: calculate_factorial(n)
# Compute the factorial of a and b.
# If either number is negative, raise an error.
# 5. Count Even and Odd Numbers Between a and b
# Function Name: count_even_odd(a, b)
# Return the count of even and odd numbers in the range from a to b.

import logging

logging.basicConfig(level=logging.INFO,filename="log.txt",filemode='w',
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt="%D/%m/%Y %H:%M")

def find_primes(a, b):
    if a > b:
        a, b = b, a
    primes = []
    for num in range(max(2, a), b + 1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    logging.info(f"Primes between {a} and {b}: {primes}")
    return primes

def fibonacci_series(length):
    if length <= 0:
        raise ValueError("Fibonacci length must be positive.")
    fib = [0, 1]
    for _ in range(2, length):
        fib.append(fib[-1] + fib[-2])
    result = fib[:length]
    logging.info(f"Fibonacci series of length {length}: {result}")
    return result

def sum_of_digits(n):
    total = sum(int(digit) for digit in str(abs(n)))
    logging.info(f"Sum of digits of {n}: {total}")
    return total

def calculate_factorial(n):
    if n < 0:
        raise ValueError("Cannot compute factorial of negative number.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    logging.info(f"Factorial of {n}: {result}")
    return result

def count_even_odd(a, b):
    if a > b:
        a, b = b, a
    even = sum(1 for i in range(a, b + 1) if i % 2 == 0)
    odd = (b - a + 1) - even
    logging.info(f"Even numbers between {a} and {b}: {even}, Odd numbers: {odd}")
    return even, odd

def main():
    try:
        a = int(input("Enter first integer (a): "))
        b = int(input("Enter second integer (b): "))

        primes = find_primes(a, b)
        print("Primes between a and b:", primes)

        fib = fibonacci_series(b)
        print(f"Fibonacci series of length {b}:", fib)

        print(f"Sum of digits of a: {sum_of_digits(a)}")
        print(f"Sum of digits of b: {sum_of_digits(b)}")

        print(f"Factorial of a: {calculate_factorial(a)}")
        print(f"Factorial of b: {calculate_factorial(b)}")

        even, odd = count_even_odd(a, b)
        print(f"Even numbers: {even}, Odd numbers: {odd}")

    except ValueError as e:
        logging.error(f"Invalid input or operation: {e}")
        print("Error:", e)

if __name__ == "__main__":
    main()
