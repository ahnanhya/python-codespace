n=int(input("enter number of key-value pairs in the dictionery:"))

my_dict={}
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")

    my_dict[key]=value

for key, value in my_dict.items():
    print(f" key: {key} , value : {value}")