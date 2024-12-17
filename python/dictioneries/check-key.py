n=int(input("enter number of key-value pairs in the dictionery:"))

my_dict={}
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")

    my_dict[key]=value

key_check=input("enter the key to check:")
if key_check in my_dict:
    print("it is present .")
else:
    print("it is not present .")
