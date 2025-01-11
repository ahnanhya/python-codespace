*PROGRAM 10:*

*TITLE:* Train Ticket Reservation System using Exception Handling

*Question:* Write a Python program to book train tickets, validate inputs for berth type, time slot, and number of tickets, and calculate the total cost.

*Aim:* To develop a Python program for booking train tickets, where the user selects the berth type, time slot, and number of tickets, with input validation and cost calculation.

*Algorithm:*

Step 1: Start the program.
Step 2: Define the TrainBooking class with attributes: source, destination, available_seats, berth_types, and time_slots.
Step 3: Create a method `book_ticket()` to validate ticket quantity, berth and time choices, calculate the total cost as ₹1000 per ticket, and display the booking details while confirming the booking.
Step 4: Take user input for berth choice, time slot choice, and number of tickets.
Step 5: Call the book_ticket() method with the user's choices.
Step 6: Handle invalid inputs with error messages using try-except.
Step 7: Stop the program

*PROGRAM:*

class TrainBooking:
    def __init__(self, source, destination, available_seats, berth_types, time_slots):
            self.source = source
                    self.destination = destination
                            self.available_seats = available_seats
                                    self.berth_types = berth_types
                                            self.time_slots = time_slots
                                                def book_ticket(self, num_tickets, berth_choice, time_choice):
                                                        try:
                                                                    if num_tickets <= 0 or num_tickets > self.available_seats:
                                                                                    raise ValueError("Invalid ticket quantity.")
                                                                                                if not (1 <= berth_choice <= len(self.berth_types)) or not (1 <= time_choice <= len(self.time_slots)):
                                                                                                                raise ValueError("Invalid berth or time choice.")
                                                                                                                            self.available_seats -= num_tickets
                                                                                                                                        print(f"Booking Details: {self.source} to {self.destination} \n"
                                                                                                                                                          f"Berth Type: {self.berth_types[berth_choice-1]} \nTime Slot: {self.time_slots[time_choice-1]} \n"
                                                                                                                                                                            f"Total Tickets: {num_tickets} \n\nTotal Cost: ₹{1000 * num_tickets}")
                                                                                                                                                                                        print(f"Successfully booked {num_tickets} ticket(s).")
                                                                                                                                                                                                except ValueError as e:
                                                                                                                                                                                                            print(f"Error: {e}")

                                                                                                                                                                                                            # Initialize booking system
                                                                                                                                                                                                            train = TrainBooking("Coimbatore", "Chennai", 100, ["Sleeper", "AC Chair", "AC Sleeper"], ["6:00 AM", "2:00 PM", "6:00 PM", "10:00 PM"])

                                                                                                                                                                                                            # User input for booking
                                                                                                                                                                                                            try:
                                                                                                                                                                                                                print("\nBerths: \n1. Sleeper \n2. AC Chair \n3. AC Sleeper")
                                                                                                                                                                                                                    berth_choice = int(input("Choose Berth: "))
                                                                                                                                                                                                                        print("\nTimes: \n1. 6:00 AM \n2. 2:00 PM \n3. 6:00 PM \n4. 10:00 PM")
                                                                                                                                                                                                                            time_choice = int(input("\nChoose Time: "))
                                                                                                                                                                                                                                num_tickets = int(input("\nEnter Number of Tickets: "))
                                                                                                                                                                                                                                    train.book_ticket(num_tickets, berth_choice, time_choice)
                                                                                                                                                                                                                                    except ValueError:
                                                                                                                                                                                                                                        print("Invalid input!")

                                                                                                                                                                                                                                        *OUTPUT:*

                                                                                                                                                                                                                                        Berths: 
                                                                                                                                                                                                                                        1. Sleeper 
                                                                                                                                                                                                                                        2. AC Chair 
                                                                                                                                                                                                                                        3. AC Sleeper
                                                                                                                                                                                                                                        Choose Berth:  2

                                                                                                                                                                                                                                        Times: 
                                                                                                                                                                                                                                        1. 6:00 AM 
                                                                                                                                                                                                                                        2. 2:00 PM 
                                                                                                                                                                                                                                        3. 6:00 PM 
                                                                                                                                                                                                                                        4. 10:00 PM

                                                                                                                                                                                                                                        Choose Time:  2

                                                                                                                                                                                                                                        Enter Number of Tickets:  2
                                                                                                                                                                                                                                        Booking Details: Coimbatore to Chennai 
                                                                                                                                                                                                                                        Berth Type: AC Chair 
                                                                                                                                                                                                                                        Time Slot: 2:00 PM 
                                                                                                                                                                                                                                        Total Tickets: 2 

                                                                                                                                                                                                                                        Total Cost: ₹2000
                                                                                                                                                                                                                                        Successfully booked 2 ticket(s).