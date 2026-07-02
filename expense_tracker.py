def display_menu():
    print("Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate total Spendings")
    print("4. Search by category")
    print("5. Exit")


def create_expense():
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
        # for each of the expenses in the list print their Title, Amount, and Category using their respective keys.
        for expense in expenses:
            print("Title    : ", expense["Title"])
            print("Amount   : ", expense["Amount"])
            print("Category : ", expense["Category"])


def calculate_spendings(expenses):  # passing the entire list of expenses
    # initializing the accumulator variable "total" to 0. Think of it like a calculator that shows 0 before you start adding values in it.
    total = 0
    for expense in expenses:
        total += expense[
            "Amount"
        ]  # fetches the amount from that expense dictionary -> adds that to the total (accumulator)
    print("Total spendings: ", total)


def search_by_category(expenses):
    category = input("Enter the category to search: ")
    found = False  # found is a flag variable used when you need to find a match between things. found = False, means you have not found any match yet.
    for expense in expenses:  # This loops through every dictionatry in the list, prints one dictionary in each iteration
        if expense["Category"].lower() == category.lower():  #
            print("Title: ", expense["Title"])
            print("Amount: ", expense["Amount"])
            print("Category: ", expense["Category"])

            found = True  # This tells python that atleast one matching pair exists
    if not found:  # If found is still false, so no expense has been found -> so "not found" = True, whereas if atlease 1 expense matched then found = True, then "not true" = false
        print("No expenses found in this category!")


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
            expense = create_expense()
            expenses.append(expense)
            print("Expenses added successfully!")
        elif choice == "2":
            display_expense(expenses)
        elif choice == "3":
            calculate_spendings(expenses)
        elif choice == "4":
            search_by_category(expenses)
        elif choice == "5":
            print("Thank you for using Expense Tracker")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
