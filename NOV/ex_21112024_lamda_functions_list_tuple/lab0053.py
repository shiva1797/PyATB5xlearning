# Write a program to calcuclate even and odd
# def find_even_odd(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")


# find_even_odd(5)
n = int(input("enter number\n="))
op = lambda num : "even" if num%2==0  else "odd"
print(op(n))

