expense = []

while True:
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")
    choice = input("choose an option: ")
    if choice == "1":
        category = input("category: ")
        amount = float(input("amount: "))
        expense.append((category, amount))
        print("Expense added!")
    elif choice == "2":
        total = 0
        print("Your expenses:")
        for category, amount in expense:
            print(category, "-", amount)
            total += amount
        print("Total:", total)
    elif choice == "3":
        print("Goodbye!")
        break