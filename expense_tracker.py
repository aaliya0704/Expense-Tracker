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
    for expense in expenses:
        print("Title    : ", expense["Title"])
        print("Amount   : ", expense["Amount"])
        print("Category : ", expense["Category"])


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

    display_expense(expenses)


if __name__ == "__main__":
    main()
