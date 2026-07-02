def display_menu():
    print("Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate total Spendings")
    print("4. Search by category")
    print("5. Save your Expenses")
    print("6. Exit")


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


def save_expenses(expenses):
    with (
        open("expenses.txt", "w") as file
    ):  # This opens the expenses.txt file in write mode. The with statement automatically closes the file once you are done
        for expense in (
            expenses
        ):  # loop through every expense in the list, with one expense at a time
            # 1st iteration-> python goes to the 1st expense.
            file.write(
                f"{expense['Title']}, {expense['Amount']}, {expense['Category']}"
            )

            # if the 1st expense is: expense = {
            # "Title": "Pizza",
            # "Amount": 450,
            # "Category": "Food"  }
            # then python does:
            # expense["Title"] becomes Pizza
            # expense["Amount"] becomes 450
            # expense["Category"] becomes Food
            # Pyhton writes them to the expenses.txt file as:
            # file.write("Pizza, 450, Food")
            # so the file now containes: Pizza, 450, Food

            # 2nd Iteration-> the loop goes back to the start and executes the 2nd expense -> writes that to the file.
            # 3rd Iteration-> the loop goes back to the start and executes the 3rd expense -> writes it to the file.
            # 4th Iteration-> the loop goes back to the start and sees if there are any expenses left -> if no, then Loop finishes

        print(
            "Expenses saved successfully"
        )  # At the end it prints "expense saved successfully"


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
            save_expenses(expenses)

        elif choice == "6":
            print("Thank you for using Expense Tracker")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
