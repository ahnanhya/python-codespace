num=input("enter numbers with spaces:")
lst=num.split()
tuple=tuple(lst)

element=input("enter an element to count occurences:")

count=tuple.count(element)

print(f"the element {element} occurs {count} times in the tuple.")