# Find the first non-repeating character in a string using sets.
# swiss -> s -x , w - Anwser

def first_non_repeating(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None

input_data = input("enter input")
print(first_non_repeating(input_data))
