# Product management using a dictionary

products = {}

while True:
    print("\n--- Product Management ---")
    print("1. Add product")
    print("2. View products")
    print("3. Update product")
    print("4. Delete product")
    print("5. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        product_id = input("Product ID: ").strip()

        if product_id in products:
            print("Product already exists.")
            continue

        name = input("Product name: ").strip()

        try:
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))

            products[product_id] = {
                "name": name,
                "price": price,
                "quantity": quantity
            }
            print("Product added successfully.")

        except ValueError:
            print("Price must be numeric and quantity must be an integer.")

    elif choice == "2":
        if not products:
            print("No products found.")
        else:
            for product_id, details in products.items():
                print(product_id, details)

    elif choice == "3":
        product_id = input("Product ID to update: ").strip()

        if product_id in products:
            name = input("New product name: ").strip()

            try:
                price = float(input("New price: "))
                quantity = int(input("New quantity: "))

                products[product_id] = {
                    "name": name,
                    "price": price,
                    "quantity": quantity
                }
                print("Product updated successfully.")
            except ValueError:
                print("Invalid price or quantity.")
        else:
            print("Product not found.")

    elif choice == "4":
        product_id = input("Product ID to delete: ").strip()

        if product_id in products:
            del products[product_id]
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")