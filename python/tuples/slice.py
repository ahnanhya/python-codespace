num=input("enter numbers with spaces:")
lst=num.split()
tuple=tuple(lst)

sliced_tuple=tuple[2:4]

print(f"the tuple is {tuple}.")
print(f"the sliced tuple is {sliced_tuple}.")