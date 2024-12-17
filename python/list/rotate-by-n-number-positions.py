def rotate_list(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]

num=input("enter numbers with spaces:")
lst=num.split()

n=int(input("enter the number from which it shld be rotated:"))
print(rotate_list(lst, n)) 
