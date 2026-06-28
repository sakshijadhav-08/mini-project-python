expenses = []
budget = float(input("Enter Monthly Budget: "))

while True:
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Summary")
    print("4. Budget Report")
    print("5. Exit")

    choice = input("Enter Choice: ")

    # Add Expense
    if choice == "1":
        desc = input("Enter Description: ")
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))
        date = input("Enter Date (DD-MM-YYYY): ")

        expenses.append([desc, category, amount, date])

        print("Expense Added Successfully!")

    # View Expenses
    elif choice == "2":
        if len(expenses) == 0:
            print("No Expenses Found!")
        else:
            sr = 1
            for e in expenses:
                print(sr, "|", e[0], "|", e[1], "| Rs.", e[2], "|", e[3])
                sr += 1

    # Category Summary
    elif choice == "3":
        summary = {}

        for e in expenses:
            category = e[1]
            amount = e[2]

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

        print("\n===== CATEGORY SUMMARY =====")
        for cat, total in summary.items():
            print(cat, ":", total)

    # Budget Report
    elif choice == "4":
        total_spent = 0

        for e in expenses:
            total_spent += e[2]

        remaining = budget - total_spent
        used = (total_spent / budget) * 100

        print("\n===== BUDGET REPORT =====")
        print("Total Spent : Rs.", total_spent)
        print("Budget Limit : Rs.", budget)
        print("Remaining : Rs.", remaining)
        print("Used :", round(used, 2), "%")

        if used >= 100:
            print("WARNING: Budget Exceeded!")
        elif used >= 80:
            print("WARNING: You have used more than 80% of your budget!")

        # Top Spending Category
        summary = {}

        for e in expenses:
            category = e[1]
            amount = e[2]

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

        if len(summary) > 0:
            top_category = max(summary, key=summary.get)
            print("Top Category :", top_category,
                  "(Rs.", summary[top_category], ")")

    # Exit
    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice!")