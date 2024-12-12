num=input("enter numbers with spaces:")
lst=num.split()
tuple=tuple(lst)

element=input("enter the element to be found:")

index=tuple.index(element)

print(f"the index of {element} in the tuple is {index}.")