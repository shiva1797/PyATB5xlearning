#Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal),
# or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

side_a = int(input("enter side a:"))
side_b = int(input("enter side b:"))
side_c = int(input("enter side c:"))

if side_a == side_b ==side_c:
    print("equilateral")
elif(side_a == side_b != side_c) or (side_a!= side_b == side_c) or (side_a==side_c != side_b):
    print("isosceles")
else:
    print("scalene")







