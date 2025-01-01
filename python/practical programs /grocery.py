def add_item(cart):
    item = input("Enter item name: ")
    price = float(input(f"Enter price of {item}: ₹"))
    quantity = int(input(f"Enter quantity of {item}: "))
    cart.append((item, price, quantity))

def display_bill(cart):
    print("\n------ Your Bill ------")
    total = 0
    for item, price, quantity in cart:
        total += price * quantity
        print(f"{item} x {quantity} = ₹{price * quantity:.2f}")
    print(f"Total Bill: ₹{total:.2f}\n")

def grocery_store():
    cart = []
    while True:
        choice = input("1. Add Item  2. View Bill  3. Exit: ")
        if choice == "1":
            add_item(cart)
        elif choice == "2":
            display_bill(cart)
        elif choice == "3":
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice.")

grocery_store()

