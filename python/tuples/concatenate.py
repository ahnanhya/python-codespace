num1=input("enter numbers with spaces:")
lst1=num1.split()
tuple1=tuple(lst1)

num2=input("enter numbers with spaces:")
lst2=num2.split()
tuple2=tuple(lst2)

result=tuple1+tuple2

print(f"the final tuple after concatinating the two tuples is {result}")