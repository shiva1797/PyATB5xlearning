#  Remove duplicate values from a dictionary.

my_dict = {"a": 1, "b": 2, "c": 1, "d": 3}
# Output: {'a': 1, 'b': 2, 'd': 3}

unique_value = set()

result = {}
for i, j in my_dict.items():
    if j not in unique_value:
        result[i] = j
        unique_value.add(j)

print(result)
