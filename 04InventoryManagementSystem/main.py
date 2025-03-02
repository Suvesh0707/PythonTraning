products = []

initial_products = [
    {"product_id": 101, "name": "Apple", "price": 0.50, "stock": 100},
    {"product_id": 102, "name": "Banana", "price": 0.30, "stock": 150},
    {"product_id": 103, "name": "Orange", "price": 0.60, "stock": 200},
    {"product_id": 104, "name": "Grapes", "price": 2.00, "stock": 50}
]

for product in initial_products:
    products.append(product)

while True:
    print("\nInventory Management System")
    print("1. Add a New Product")
    print("2. Update Stock for an Existing Product")
    print("3. Sell a Product")
    print("4. Display Inventory")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        product_id = int(input("Enter Product ID: "))
        product_exists = False
        for product in products:
            if product["product_id"] == product_id:
                product_exists = True
                break
        if product_exists:
            print("Product ID already exists. Try again.")
        else:
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            stock = int(input("Enter Product Stock: "))
            products.append({
                "product_id": product_id,
                "name": name,
                "price": price,
                "stock": stock
            })
            print("Product added successfully!")

    elif choice == "2":
        product_id = int(input("Enter Product ID to update stock: "))
        product_found = False
        for product in products:
            if product["product_id"] == product_id:
                new_stock = int(input("Enter new stock quantity: "))
                product["stock"] = new_stock
                print("Stock updated successfully!")
                product_found = True
                break
        if not product_found:
            print("Product not found.")

    elif choice == "3":
        product_id = int(input("Enter Product ID to sell: "))
        product_found = False
        for product in products:
            if product["product_id"] == product_id:
                quantity = int(input("Enter quantity to sell: "))
                if product["stock"] >= quantity:
                    product["stock"] -= quantity
                    total_price = quantity * product["price"]
                    print(f"Sold {quantity} units of {product['name']}. Total: ${total_price:.2f}")
                else:
                    print("Out of stock or insufficient quantity.")
                product_found = True
                break
        if not product_found:
            print("Product not found.")

    elif choice == "4":
        if not products:
            print("Inventory is empty.")
        else:
            print("\nCurrent Inventory:")
            print(f"{'ID':<5} {'Name':<15} {'Price':<10} {'Stock':<10}")
            print("-" * 40)
            for product in products:
                print(f"{product['product_id']:<5} {product['name']:<15} ${product['price']:<10.2f} {product['stock']:<10}")
            print()

    elif choice == "5":
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
