
print("printing prime numbers between two intervals")
lwr = int(input("enter the starting of the range:"))

upr = int(input("enter the ending of the range:"))

print(f"Prime numbers between {lwr} and {upr} are:")

for numb in range(lwr, upr + 1):
    if numb > 1:
        for a in range(2, numb):
            if (numb % a) == 0:
                break
        else:
                print(numb)