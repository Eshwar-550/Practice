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