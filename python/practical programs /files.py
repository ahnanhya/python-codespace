def save_contact():
    with open("contacts.txt", "a") as file:
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        file.write(f"{name.strip()}, {phone.strip()}, {email.strip()}\n")  # Strip to avoid unwanted spaces
    print("Contact saved! You can view the formatted contact list in 'contacts.txt'.")

def format_and_save_contacts():
    try:
        with open("contacts.txt", "r") as file:
            lines = file.readlines()
        
        with open("contacts.txt", "w") as file:
            file.write(f"{'Line':<5} {'Name':<20} {'Phone No':<15} {'Email ID':<25}\n{'-'*65}\n")
            for i, line in enumerate(lines, 1):
                if line.strip():  # Ensure the line is not empty
                    parts = line.strip().split(",")
                    if len(parts) == 3:  # Ensure the line has exactly 3 parts
                        name, phone, email = [x.strip() for x in parts]  # Strip extra spaces
                        file.write(f"{i:<5}{name:<20}{phone:<15}{email:<25}\n")
                    else:
                        print(f"Skipping invalid line {i}: {line.strip()}")
        print("Contacts formatted and saved to 'contacts.txt'.")
    except FileNotFoundError:
        print("No contacts found. Save a contact first.")

while True:
    choice = input("\nEMPLOYEE CONTACT DETAILS ENTRY USING FILES\n\n1. Save Contact\n2. Format and Save Contacts\n3. Exit\nEnter choice: ")
    if choice == "1": save_contact()
    elif choice == "2": format_and_save_contacts()
    elif choice == "3": break
    else: print("Invalid choice. Try again!")
