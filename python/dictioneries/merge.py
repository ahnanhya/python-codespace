#dict 1
n=int(input("enter number of key-value pairs in the dictionery:"))

dict1={}
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")

    dict1[key]=value

#dict 2
n=int(input("enter number of key-value pairs in the dictionery:"))

dict2={}
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")

    dict2[key]=value

merge= {**dict1,**dict2}

print(f"merged dictionery is {merge}")