import random
import string

class SeatBookingSystem:
    def __init__(self, rows, columns):
        """
        Initializes the seating chart for Apache Airlines' Burak757.
        Rows represent the number of rows of seats.
        Columns represent the letters assigned per row (excluding aisles 'X' and storage 'S').
        Also initializes a dictionary to store booking references and customer data linked to specific seats.
        """
        self.seating_chart = {}
        self.booking_data = {}
        valid_seats = 'ABCDEF'

        # Initialize seating for each row except special cases
        for i in range(1, rows + 1):
            for letter in valid_seats:
                if i == 4 and letter in {'D', 'E', 'F'}:
                    self.seating_chart[f'{i}{letter}'] = 'S'  # Storage area
                else:
                    self.seating_chart[f'{i}{letter}'] = 'F'

    def check_availability(self, seat):
        """
        Checks if the specified seat is available for booking.
        """
        return self.seating_chart.get(seat, 'Invalid') == 'F'

    def book_seat(self, seat, customer_name, customer_email):
        """
        Books a seat if it is available, and stores the customer data along with a unique booking reference.
        """
        if self.check_availability(seat):
            reference = self.generate_unique_reference()
            self.seating_chart[seat] = 'R'
            self.booking_data[seat] = {
                'reference': reference,
                'name': customer_name,
                'email': customer_email
            }
            return f"Seat {seat} booked successfully with reference {reference}."
        else:
            return f"Seat {seat} cannot be booked."

    def free_seat(self, seat):
        """
        Frees a seat if it is currently booked and removes any associated booking details.
        """
        if self.seating_chart.get(seat) == 'R':
            self.seating_chart[seat] = 'F'
            del self.booking_data[seat]  # Remove booking details
            return f"Seat {seat} is now free."
        else:
            return f"Seat {seat} is not currently booked or is invalid."

    def generate_unique_reference(self):
        """
        Generates a unique booking reference using random alphanumeric characters.
        Ensures that each booking reference is unique by comparing with existing ones in the booking data.
        """
        while True:
            reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            if all(reference != data['reference'] for data in self.booking_data.values()):
                return reference

# Example usage:
system = SeatBookingSystem(80, 6)  # Initialize for 80 rows, 6 potential seat columns per row

def main():
    while True:
        print("\nMenu:")
        print("1. Book a seat")
        print("2. Free a seat")
        print("3. Exit program")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            seat = input("Enter the seat to book (e.g., 1A): ")
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            result = system.book_seat(seat, name, email)
            print(result)
        
        elif choice == '2':
            seat = input("Enter the seat to free (e.g., 1A): ")
            result = system.free_seat(seat)
            print(result)
        
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

main()
