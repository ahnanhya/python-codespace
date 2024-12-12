num=input("enter numbers with spaces:")
lst=num.split()

#list to tuple
tuple=tuple(lst)
print(f"the tuple form is {tuple}")

#tuple to list 
lst=list(tuple)
print(f"the list form is {lst}")