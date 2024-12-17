n=int(input("enter number of key-value pairs in the dictionery:"))

my_dict={}
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")

    my_dict[key]=value 


key_list=list(my_dict.keys())

value_list=list(my_dict.values())

print(f"the key and value lists are {key_list} , {value_list}")