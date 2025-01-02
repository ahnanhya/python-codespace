def largest(a, b, c):
    return max(a, b, c)

num1= int(input("enter a number:"))
num2= int(input("enter a number:"))
num3= int(input("enter a number:"))
print(f"The largest number among {num1}, {num2}, and {num3} is {largest(num1, num2, num3)}")
