# Student Management System

students = {}

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        students[roll_no] = name
        print("Student added successfully!")

    elif choice == "2":
        if students:
            print("\nStudent Records:")
            for roll, name in students.items():
                print(f"Roll No: {roll}, Name: {name}")
        else:
            print("No student records found.")

    elif choice == "3":
        roll_no = input("Enter Roll Number to search: ")
        if roll_no in students:
            print(f"Student Found: {students[roll_no]}")
        else:
            print("Student not found.")

    elif choice == "4":
        roll_no = input("Enter Roll Number to delete: ")
        if roll_no in students:
            del students[roll_no]
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")