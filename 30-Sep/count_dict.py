# How do you count the occurrences of each element in a list using a dictionary?

list1 = ['apple','banana','kiwi','apple','orange','apple']
count = {}
for i in list1:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)