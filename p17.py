# Student Record Management System

students = {}

while True:
    print("\n===== STUDENT RECORD SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Marks: ")

        students[roll_no] = {
            "name": name,
            "marks": marks
        }

        print("Student Added Successfully!")

    elif choice == "2":
        if students:
            print("\n----- STUDENT RECORDS -----")
            for roll_no, details in students.items():
                print(f"Roll No: {roll_no}")
                print(f"Name   : {details['name']}")
                print(f"Marks  : {details['marks']}")
                print("-" * 25)
        else:
            print("No student records found!")

    elif choice == "3":
        roll_no = input("Enter Roll Number to Search: ")

        if roll_no in students:
            print("\nStudent Found!")
            print("Name :", students[roll_no]["name"])
            print("Marks:", students[roll_no]["marks"])
        else:
            print("Student Not Found!")

    elif choice == "4":
        roll_no = input("Enter Roll Number to Delete: ")

        if roll_no in students:
            del students[roll_no]
            print(" Student Deleted Successfully!")
        else:
            print(" Student Not Found!")

    elif choice == "5":
        print("Program Closed Successfully!")
        break

    else:
        print("Invalid Choice! Try Again.")