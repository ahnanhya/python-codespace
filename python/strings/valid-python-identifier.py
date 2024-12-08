
s=input("enter a string to check whether it is valid:")

def is_valid_identifier(s):
    return s.isidentifier()

print("'valid=true'")
print("'not valid=false'")

print(is_valid_identifier(s))