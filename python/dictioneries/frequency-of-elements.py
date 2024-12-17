from collections import counter

n=int(input("enter number of key-value pairs in the dictionery:"))

my_dict={}
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")

    my_dict[key]=value

value_freq= Counter(my_dict.values())


print(f" the frequency is {value_freq}")