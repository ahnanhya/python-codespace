def power(base, exponent):
    return base ** exponent

base=int(input("enter a number for the base:"))
exponent = int(input("enter a number for the exponent:"))
print(f"{base} raised to the power of {exponent} is {power(base, exponent)}")
