num=input("enter numbers with spaces:")
lst=num.split()

element= input("enter the element to check in the list:")

if(element in lst):
    print(f"the element {element} exists in the list.")
else:
    print(f"the element {element} does not exist.")