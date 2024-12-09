num=input("enter numbers with spaces:")
lst=num.split()

value=input("enter the value to count for occurences:")

count=lst.count(value)

print(f"the value {value} occurs {count} times")