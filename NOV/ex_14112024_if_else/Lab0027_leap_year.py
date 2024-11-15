#leap year

year = int(input("enter year"))

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("its leap year")
else:
    (print("its not a leap year"))

