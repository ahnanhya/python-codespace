year = int(input("enter the year to check whether it is a leap year:"))

if (year % 400 == 0):
    print(f"{year} is a leap year")

elif (year % 4 ==0):
    print(f"{year} is a leap year")

else:
    print(f"{year} is not a leap year")