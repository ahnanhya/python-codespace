# menus
print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
print("5.modulus")

# input choice
ch=int(input("Enter Choice(1-5): "))

if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print(f"Sum = {c}")
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print(f"Difference = {c}")
elif  ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print(f"Product = {c}")
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print(f"Quotient = {c}")
elif ch==5:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a%b
    print(f"reminder = {c}")
else:
    print("Invalid Choice")
