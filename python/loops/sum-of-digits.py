num = int(input("enter a number with two or more digits: "))

#extract last digit
r = num % 10

#extract first digit by removing last digit 
n = num // 10

sum=r+n

print(f"the sum of the digits in the number {num} is {sum}")