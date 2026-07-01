def create_expense():
    title = input("Enter expense title: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")

    expense = {
        "Title": title,
        "Amount": amount,
        "Category": category,
    }
    return expense


def display_expense(expenses):
    for expense in expenses:  # for each of the expenses in the list print their Title, Amount, and Category using their respective keys
        print("Title    : ", expense["Title"])
        print("Amount   : ", expense["Amount"])
        print("Category : ", expense["Category"])


def calculate_total(expenses):  # passing the entire list of expenses
    total = 0  # initializing the accumulator variable total to 0. Think of it like a calculator that shows 0 before you start adding values in it. This is important because if you don't initialize it, the program won't know what to add to and will throw an error.
    for expense in expenses:
        total += expense[
            "Amount"
        ]  # fetches the amount from that expense dictionary -> adds that to the total (accumulator).
    print("total spendings: ", total)


def main():
    print("=" * 40)
    print("         Python Expense Tracker")
    print("=" * 40)
    print()
    print("Track and manage your daily expenses!")
    print()

    # Creating an expense:
    expense = create_expense()

    # creating an empty list to store expenses:
    expenses = []

    # Adding the created expense to the expense list:
    expenses.append(expense)
    print("Your expenses are as shown below: ")

    # calling the display_expanse function to diplay each expense of the list
    display_expense(expenses)

    # calling the calculate_taotal() function to calculate the total spendings
    calculate_total(expenses)


if __name__ == "__main__":
    main()
