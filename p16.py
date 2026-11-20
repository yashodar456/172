

balance = 1000

while True:
    print("\n====== BANK MANAGEMENT SYSTEM ======")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"\nCurrent Balance: ₹{balance}")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₹"))

        if amount > 0:
            balance += amount
            print(f"₹{amount} Deposited Successfully!")
            print(f" New Balance: ₹{balance}")
        else:
            print(" Invalid Amount!")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount <= balance:
            balance -= amount
            print(f" ₹{amount} Withdrawn Successfully!")
            print(f" Remaining Balance: ₹{balance}")
        else:
            print("Insufficient Balance!")

    elif choice == "4":
        print("Thank You For Banking With Us!")
        break

    else:
        print(" Invalid Choice! Please try again.")