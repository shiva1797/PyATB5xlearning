import math
try:
# OverflowError: math range error
    print(math.exp(10000))
except Exception as e:
    print(e)


try:
    num1 = int(input("Enter a Number 1\n"))
    num2 = int(input("Enter a Number 2\n"))
    result = num1 / num2
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("Output is ", result)
