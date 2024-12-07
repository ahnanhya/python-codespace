a=int(input("enter side1:"))
b=int(input("enter side2:"))
c=int(input("enter side3:"))

if(a==b and b==c):
    print("equilateral triangle.")
elif(a==b or b==c or a==c ):
    print("isosceles triangle.")
else:
    print("scalene triangle.")