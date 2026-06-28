inventory = {}

while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Stock In")
    print("3. Stock Out")
    print("4. View Inventory")
    print("5. Low Stock Alert")
    print("6. Report")
    print("7. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        pid = input("Enter Product ID: ")

        if pid in inventory:
            print("Product ID Already Exists!")
        else:
            name = input("Enter Product Name: ")
            category = input("Enter Category: ")
            price = float(input("Enter Price: "))
            qty = int(input("Enter Quantity: "))
            reorder = int(input("Enter Reorder Level: "))

            inventory[pid] = {
                "name": name,
                "category": category,
                "price": price,
                "qty": qty,
                "reorder": reorder
            }

            print("Product Added Successfully!")

    elif choice == 2:
        pid = input("Enter Product ID: ")

        if pid in inventory:
            add_qty = int(input("Enter Quantity to Add: "))
            inventory[pid]["qty"] += add_qty
            print("Stock Updated!")
        else:
            print("Product Not Found!")

    elif choice == 3:
        pid = input("Enter Product ID: ")

        if pid in inventory:
            remove_qty = int(input("Enter Quantity to Remove: "))

            if remove_qty <= inventory[pid]["qty"]:
                inventory[pid]["qty"] -= remove_qty
                print("Stock Removed!")
            else:
                print("Not Enough Stock!")
        else:
            print("Product Not Found!")

    elif choice == 4:
        print("\n----- INVENTORY -----")

        for pid, data in inventory.items():
            print("ID:", pid)
            print("Name:", data["name"])
            print("Category:", data["category"])
            print("Price:", data["price"])
            print("Quantity:", data["qty"])
            print("Reorder Level:", data["reorder"])
            print()

    elif choice == 5:
        print("\n----- LOW STOCK ALERT -----")

        for pid, data in inventory.items():
            if data["qty"] <= data["reorder"]:
                print(data["name"], "- Low Stock")

    elif choice == 6:
        total_products = len(inventory)
        total_value = 0
        categories = set()

        for data in inventory.values():
            total_value += data["price"] * data["qty"]
            categories.add(data["category"])

        print("\n----- INVENTORY REPORT -----")
        print("Total Products:", total_products)
        print("Total Stock Value:", total_value)
        print("Categories:", ", ".join(categories))

    elif choice == 7:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")