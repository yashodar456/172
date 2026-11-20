# Train Reservation System

seats = 20
bookings = {}

while True:
    print("\n===== TRAIN RESERVATION SYSTEM =====")
    print("1. Book Ticket")
    print("2. View Booking")
    print("3. Cancel Ticket")
    print("4. Check Available Seats")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if seats > 0:
            name = input("Enter Passenger Name: ")
            age = input("Enter Passenger Age: ")

            ticket_id = len(bookings) + 1

            bookings[ticket_id] = {
                "name": name,
                "age": age
            }

            seats -= 1

            print("\nTicket Booked Successfully!")
            print("Ticket ID:", ticket_id)
        else:
            print("No Seats Available!")

    elif choice == "2":
        ticket_id = int(input("Enter Ticket ID: "))

        if ticket_id in bookings:
            print("\n===== BOOKING DETAILS =====")
            print("Passenger:", bookings[ticket_id]["name"])
            print("Age:", bookings[ticket_id]["age"])
            print("Ticket ID:", ticket_id)
        else:
            print("Booking Not Found")

    elif choice == "3":
        ticket_id = int(input("Enter Ticket ID to Cancel: "))

        if ticket_id in bookings:
            del bookings[ticket_id]
            seats += 1
            print("Ticket Cancelled Successfully")
        else:
            print("Ticket Not Found")

    elif choice == "4":
        print(f"Available Seats: {seats}")

    elif choice == "5":
        print("Thank You For Using Train Reservation System")
        break

    else:
        print("Invalid Choice")