num1=input("enter a set of numbers with spaces:")
lst1=num1.split()

num2=input("enter another set of numbers with spaces:")
lst2=num2.split()

add=sorted(lst1+lst2)

print(f"the addes list is {add}")