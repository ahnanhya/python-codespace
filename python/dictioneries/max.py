n=int(input("enter number of key-value pairs in the dictionery:"))

my_dict={}
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")

    my_dict[key]=value

max_key=max(my_dict,key=my_dict.get)

print(f"the max key is {max_key}")