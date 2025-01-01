b=500
pin=1234
chances=3

print("**** welcome to SBI ****")

while chances>=0:
    x=int(input("enter pin number:"))
    if x==pin:
        print("**** login successful****")
        x=int(input("press 1 to continue: "))

        if x==1:
            print("1.check balance")
            print("2.withdraw amount")
            print("3.exit")

            d=int(input("enter your choice:"))
            if d==1:
              print("your balance is:")
              print(b)

            elif d==2:
              w=int(input("enter the amount to withdraw:"))

              if w<b:
                  print("withdrawal successful!")
                  b=b-w
            
              else:
                   print("insufficient funds")
        else:
            print("successfully logged out")
            break

    else:
            print("**** invalid password ****")

            chances=chances-1
            if chances==0:
                print("**** account blocked ****") 
                break       
            