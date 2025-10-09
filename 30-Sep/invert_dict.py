# invert a dictionary
# d = {'a': 1, 'b': 2, 'c': 3}

d = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = {value:key for key,value in d.items()}
print(inverted_dict)