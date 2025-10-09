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