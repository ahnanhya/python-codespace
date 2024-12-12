num=input("enter numbers with spaces to remove the duplicates:")
lst=num.split()

remove_duplicates=list(set(lst))

print(f"the removed list is {remove_duplicates}")