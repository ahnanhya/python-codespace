string=input("enter a string to check whether it is palindrome:")

#reversing 
reverse=string[::-1]

if(string==reverse):
    print("it is a palindrome.")
else:
    print("it is not a palindrome.")


