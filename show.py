# Movie Ticket Booking System

movies = {
    "1": {"name": "Avengers", "price": 200},
    "2": {"name": "Batman", "price": 180},
    "3": {"name": "Spider-Man", "price": 220}
}

while True:
    print("\n====== MOVIE TICKET BOOKING SYSTEM ======")
    print("1. View Movies")
    print("2. Book Ticket")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable Movies:")
        for key, movie in movies.items():
            print(f"{key}. {movie['name']} - ₹{movie['price']}")

    elif choice == "2":
        print("\nAvailable Movies:")
        for key, movie in movies.items():
            print(f"{key}. {movie['name']} - ₹{movie['price']}")

        movie_choice = input("Select movie number: ")

        if movie_choice in movies:
            tickets = int(input("Enter number of tickets: "))

            total = tickets * movies[movie_choice]["price"]

            print("\n=========== TICKET ===========")
            print("Movie :", movies[movie_choice]["name"])
            print("Tickets :", tickets)
            print("Total Amount : ₹", total)
            print("==============================")
            print("Booking Successful!")
        else:
            print("Invalid Movie Selection")

    elif choice == "3":
        print("Thank You For Visiting!")
        break

    else:
        print("Invalid Choice")