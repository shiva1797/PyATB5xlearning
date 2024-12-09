# non-repeating char in string

def non_repeat_char(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None

res=non_repeat_char("shivashiva")

print(res)
