class SeatBookingSystem:
    def __init__(self, rows, columns):
        """
        Initializes the seating chart for Apache Airlines' Burak757.
        Rows represent the number of rows of seats.
        Columns represent the letters assigned per row (excluding aisles 'X' and storage 'S').
        """
        self.seating_chart = {}
        valid_seats = 'ABCDEF'
        aisle = 'X'
        storage = 'S'
        
        # Initialize the seating chart with free seats 'F', except for aisles and storage
        for i in range(1, rows + 1):
            for letter in valid_seats:
                if i in {4} and letter in {'D', 'E', 'F'}:
                    self.seating_chart[f'{i}{letter}'] = storage
                else:
                    self.seating_chart[f'{i}{letter}'] = 'F'

    def check_availability(self, seat):
        """
        Checks if a specified seat is available for booking.
        """
        return self.seating_chart.get(seat, 'Invalid seat') == 'F'

    def book_seat(self, seat):
        """
        Books a seat if it is available.
        """
        if self.check_availability(seat):
            self.seating_chart[seat] = 'R'
            return f"Seat {seat} booked successfully."
        else:
            return f"Seat {seat} cannot be booked."

    def free_seat(self, seat):
        """
        Frees a seat if it is currently booked.
        """
        if self.seating_chart.get(seat) == 'R':
            self.seating_chart[seat] = 'F'
            return f"Seat {seat} is now free."
        else:
            return f"Seat {seat} is not currently booked."

    def show_booking_state(self):
        """
        Displays the current state of all seats.
        """
        for row in range(1, 81):  # Assuming 80 rows
            print(' '.join(f"{row}{seat}: {self.seating_chart[f'{row}{seat}']}" for seat in 'ABCDEF' if f'{row}{seat}' in self.seating_chart))

def main():
    system = SeatBookingSystem(80, 6)  # Initialize for 80 rows, 6 potential seat columns per row

    while True:
        print("\nMenu:")
        print("1. Check availability of seat")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking state")
        print("5. Exit program")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            seat = input("Enter the seat to check (e.g., 1A): ")
            available = system.check_availability(seat)
            print("Available" if available else "Not available or invalid seat")
        
        elif choice == '2':
            seat = input("Enter the seat to book (e.g., 1A): ")
            result = system.book_seat(seat)
            print(result)
        
        elif choice == '3':
            seat = input("Enter the seat to free (e.g., 1A): ")
            result = system.free_seat(seat)
            print(result)
        
        elif choice == '4':
            system.show_booking_state()
        
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
