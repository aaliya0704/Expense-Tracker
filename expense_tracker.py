def display_menu():
    print("Menu:")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Calculate total Spendings")
    print("4. Search by category")
    print("5. Exit")


def get_expense():
    title = input("Enter the expense Title: ")
    amount = float(input("Enter the expense amount: "))
    category = input("enter the expense category: ")

    expense = {
        "Title": title,
        "Amount": amount,
        "Category": category,
    }

    return expense


def display_expense(expenses):
    if len(expenses) == 0:
        print("No expenses found!")
        return
    else:
        print("Your Expenses are: ")
        for expense in expenses:
            print(expense["Title"])
            print(expense["Amount"])
            print(expense["Category"])


def calculate_spendings(expenses):
    total = 0
    for expense in expenses:
        total += expense["Amount"]
    print("Total spendings: ", total)


def main():
    print("=" * 40)
    print("PYTHON EXPENSE TRACKER")
    print("=" * 40)
    print()

    expenses = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            expense = get_expense()
            expenses.append(expense)
            print("Expenses added successfully!")
        elif choice == "2":
            display_expense(expenses)
        elif choice == "3":
            calculate_spendings(expenses)
        elif choice == "4":
            print("search feature comming next")
        elif choice == "5":
            print("Thank you for using Expense Tracker")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
