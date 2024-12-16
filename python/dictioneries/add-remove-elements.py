n=int(input("enter number of key-value pairs in the dictionery:"))

my_dict={}
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")

    my_dict[key]=value

my_dict["state"]="tamil nadu"
print(f"after adding:{my_dict}")

del my_dict["state"]
print(f"after deleting:{my_dict}")