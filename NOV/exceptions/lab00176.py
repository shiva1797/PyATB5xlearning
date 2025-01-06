from logging import exception

try:
    num1 = int(input("Enter a Number 1\n"))
    num2 = int(input("Enter a Number 2\n"))
    result = num1 / num2
except Exception as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("Output is ", result)