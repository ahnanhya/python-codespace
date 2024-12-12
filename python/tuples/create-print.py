num=input("enter numbers with spaces:")
lst=num.split()
tuple=tuple(lst)

for element in tuple:
    print("the elements of the tuple are:")
    print(element)