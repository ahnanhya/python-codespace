num=input("enter numbers with spaces:")
lst=num.split()
tuple=tuple(lst)

max=max(tuple)

min=min(tuple)

print(f"the maximum is {max} and the minimum is {min}")