n=int(input("enter number of key-value pairs in the dictionery:"))

my_dict={}
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")

    my_dict[key]=value

sorted_keys=sorted(my_dict.keys())

print(f"the sorted keys is {sorted_keys}")