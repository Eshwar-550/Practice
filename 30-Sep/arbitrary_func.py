# Write a Python function that accepts an arbitrary number of integers as input and returns their sum.
# sum_all(1, 2, 3) o/p: 6
# sum_all(5, 10, 15, 20) o/p: 50
# sum_all() o/p: 0

def sum_all(*num):
    return sum(num)

print(sum_all(1,2,3))
print(sum_all(5, 10, 15, 20))
print(sum_all())  