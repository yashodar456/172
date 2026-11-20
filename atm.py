balance = 5000
pin = "1234"

print("===== WELCOME TO ATM =====")

entered_pin = input("Enter Your 4-Digit PIN: ")

if entered_pin == pin:

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            print(f"\n Available Balance: ₹{balance}")

        elif choice == "2":
            amount = float(input("Enter Deposit Amount: ₹"))

            if amount > 0:
                balance += amount
                print("Deposit Successful")
                print(f"Updated Balance: ₹{balance}")
            else:
                print(" Invalid Amount")

        elif choice == "3":
            amount = float(input("Enter Withdrawal Amount: ₹"))

            if amount <= balance:
                balance -= amount
                print(" Withdrawal Successful")
                print(f"Remaining Balance: ₹{balance}")
            else:
                print("Insufficient Balance")

        elif choice == "4":
            new_pin = input("Enter New PIN: ")
            pin = new_pin
            print("PIN Changed Successfully")

        elif choice == "5":
            print("Thank You For Using Our ATM")
            break

        else:
            print("Invalid Choice")

else:
    print(" Incorrect PIN Access Denied")