num1=int(input("enter a number:"))
num2=int(input("enter another number:"))
num3=int(input("enter a third number:"))
  
if (num1 >= num2) and (num1 >= num3):
   largest = num1

elif (num2 >= num1) and (num2 >= num3):
   largest = num2

else:
   largest = num3

print(f"the largest is {largest}.")

