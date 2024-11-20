# User Defined
# 1. The can't return -> non return
# 2.They can return something
# 3.They have parameters
# 4. They don't parameters / arguments
import math


# 1. The can't return -> non return
# No Return Type and No Parameter / Argument - NRNP
def greet():
    print("Hello")


greet()


# 2. # No Return Type and with Argument/ Param
def greet_by_name(name):
    print(name)


greet_by_name("shiva")


# 3. No Return Type and with Default Argument ( # positional argument)
def say_hello_default_arg(name="default_name"):
    print(name.upper())


say_hello_default_arg("shiva")
say_hello_default_arg()


def multiple_args(name1="A", name2="B"):
    print(name1, name2)


multiple_args()
multiple_args("Lucky", "Sharma")
multiple_args(name1="Pramod")
multiple_args(name1="Dutta", name2="Amit")
multiple_args(name2="Amit")




# 4. Argument + return Type


def sum_of_two(a, b):
    return (a + b)


result = sum_of_two(4, 56)
print(result)


def sum_of_two_number_with_default(num1=100, num2=200):
    print("I will sum the two numbers!")
    return num1 + num2

result = sum_of_two_number_with_default(num1=34, num2=34)
print(result)
result = sum_of_two_number_with_default()
print(result)