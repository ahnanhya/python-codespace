num = int(input("enter a number with two or more digits:"))
reverse = int(str(num)[::-1])

if num == reverse:
  print(' the number is a Palindrome')
else:
  print("the number is not a Palindrome") 