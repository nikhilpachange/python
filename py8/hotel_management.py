class Hotel:
    def __init__(self):
        self.rooms = {}

    def book_room(self, guest_name, room_number):
        if room_number in self.rooms:
            print(f"Room {room_number} is already booked!")
        else:
            self.rooms[room_number] = guest_name
            print(f"Room {room_number} booked for {guest_name}.")

    def check_out(self, room_number):
        if room_number in self.rooms:
            print(f"Room {room_number} checked out successfully!")
            del self.rooms[room_number]
        else:
            print(f"Room {room_number} is not occupied!")

    def view_bookings(self):
        if self.rooms:
            print("Current Room Bookings:")
            for room, guest in self.rooms.items():
                print(f"Room {room}: {guest}")
        else:
            print("No rooms are currently booked.")

def main():
    hotel = Hotel()
    while True:
        print("\nHotel Management System")
        print("1. Book a Room")
        print("2. Check Out")
        print("3. View Bookings")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            guest_name = input("Enter guest name: ")
            room_number = input("Enter room number: ")
            hotel.book_room(guest_name, room_number)
        elif choice == '2':
            room_number = input("Enter room number to check out: ")
            hotel.check_out(room_number)
        elif choice == '3':
            hotel.view_bookings()
        elif choice == '4':
            print("Thank you for using Hotel Management System!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
