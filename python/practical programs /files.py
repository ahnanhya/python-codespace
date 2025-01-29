
def save_contact():
    with open("contacts.txt", "a") as file:
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        file.write(f"{name}, {phone}, {email}\n")
    print("Contact saved! You can view the formatted contact list in 'contacts.txt'.")

def format_and_save_contacts():
    try:
        with open("contacts.txt", "r") as file:
            lines = file.readlines()

        with open("contacts.txt", "w") as file:
            file.write(f"{'Line':<5} {'Name':<20} {'Phone No':<15} {'Email ID':<25}\n{'-'*65}\n")
            for i, line in enumerate(lines, 1):
                name, phone, email = line.strip().split(", ")
                file.write(f"{i:<5} {name:<20} {phone:<15} {email:<25}\n")
        print("Contacts formatted and saved to 'contacts.txt'.")
    except FileNotFoundError:
        print("No contacts found. Save a contact first.")

while True:
 choice = input("\nEMPLOYEE CONTACT DETAILS ENTRY USING FILES\n\n1. Save Contact\n2. Format and Save Contacts\n3. Exit\nEnter choice: ")
 if choice == "1": save_contact()
 elif choice == "2": format_and_save_contacts()
 elif choice == "3": break
 else: print("Invalid choice. Try again!")      
