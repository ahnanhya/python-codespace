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
