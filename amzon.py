# Amazon Mini Store

products = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Smartphone", "price": 20000},
    3: {"name": "Headphones", "price": 2000},
    4: {"name": "Smart Watch", "price": 5000}
}

cart = []

while True:
    print("\n AMAZON MINI STORE")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable Products:")
        for pid, product in products.items():
            print(f"{pid}. {product['name']} - ₹{product['price']}")

    elif choice == "2":
        product_id = int(input("Enter Product ID: "))

        if product_id in products:
            cart.append(products[product_id])
            print(" Product Added to Cart")
        else:
            print(" Invalid Product ID")

    elif choice == "3":
        if not cart:
            print(" Cart is Empty")
        else:
            print("\n YOUR CART ")
            total = 0

            for item in cart:
                print(f"{item['name']} - ₹{item['price']}")
                total += item['price']

            print("Total = ₹", total)

    elif choice == "4":
        if not cart:
            print(" Cart is Empty")
        else:
            total = sum(item['price'] for item in cart)

            print("\n===== BILL =====")
            for item in cart:
                print(f"{item['name']} - ₹{item['price']}")

            print("-------------------")
            print("Total Amount: ₹", total)
            print("Order Placed Successfully!")

            cart.clear()

    elif choice == "5":
        print("Thank You For Shopping!")
        break

    else:
        print(" Invalid Choice")