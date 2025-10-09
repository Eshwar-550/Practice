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