import json

# Load expenses from the JSON file
def load_data():
    try:
        with open('data/expenses.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save the expenses data to the JSON file
def save_data(data):
    with open('data/expenses.json', 'w') as file:
        json.dump(data, file, indent=4)

# Add a new expense to the expenses list
def add_expense(amount, category, date):
    expenses = load_data()
    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }
    expenses.append(expense)
    save_data(expenses)
    print(f"Added expense: {expense}")

# Display all expenses
def display_expenses():
    expenses = load_data()
    if not expenses:
        print("No expenses recorded yet.")
        return
    for expense in expenses:
        print(f"{expense['date']} - {expense['category']}: ${expense['amount']}")

# Calculate total spending by category
def spending_by_category():
    expenses = load_data()
    categories = {}
    for expense in expenses:
        category = expense['category']
        if category not in categories:
            categories[category] = 0
        categories[category] += expense['amount']
    return categories
