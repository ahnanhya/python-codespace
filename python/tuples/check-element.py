num=input("enter numbers with spaces:")
lst=num.split()
tuple=tuple(lst)

element=input("enter the element to check:")

if element in tuple :
    print(f"the element {element} exists in the tuple.")
else:
    print(f"the element {element} does not exists in the tuple.")