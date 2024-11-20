import json
from utils import load_data, save_data, add_expense, display_expenses, spending_by_category
from reports import generate_report

def main():
    print("Welcome to the Expense Tracker!")
    while True:
        print("\nChoose an option:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Spending by Category")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '1':
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            date = input("Enter the date (YYYY-MM-DD): ")
            add_expense(amount, category, date)
        
        elif choice == '2':
            display_expenses()
        
        elif choice == '3':
            categories = spending_by_category()
            for category, total in categories.items():
                print(f"{category}: ${total}")
        
        elif choice == '4':
            generate_report()
        
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
