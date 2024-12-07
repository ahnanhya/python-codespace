a=int(input("enter a number:"))
b=int(input("enter another number:"))

print(f"the numbers before swapping is {a} and {b}")

a=a+b
b=a-b
a=a-b

print(f"the numbers after swapping is {a} and {b}")

