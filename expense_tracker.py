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


def main():
    print("=" * 40)
    print("         Python Expense Tracker")
    print("=" * 40)
    print()
    print("Track and manage your daily expenses!")

    expense = create_expense()
    print("Your expenses are as shown below: ")
    print("Title:", expense["Title"])
    print("Amount:", expense["Amount"])
    print("Category:", expense["Category"])


if __name__ == "__main__":
    main()
