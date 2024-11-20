import tkinter as tk
from utils import add_expense

def add_expense_gui():
    def submit_expense():
        try:
            amount = float(amount_entry.get())
            category = category_entry.get()
            date = date_entry.get()
            add_expense(amount, category, date)
            result_label.config(text="Expense added successfully!")
        except ValueError:
            result_label.config(text="Invalid input. Please try again.")

    root = tk.Tk()
    root.title("Expense Tracker - Add Expense")

    tk.Label(root, text="Amount").grid(row=0, column=0)
    tk.Label(root, text="Category").grid(row=1, column=0)
    tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=2, column=0)

    amount_entry = tk.Entry(root)
    category_entry = tk.Entry(root)
    date_entry = tk.Entry(root)

    amount_entry.grid(row=0, column=1)
    category_entry.grid(row=1, column=1)
    date_entry.grid(row=2, column=1)

    submit_button = tk.Button(root, text="Add Expense", command=submit_expense)
    submit_button.grid(row=3, column=0, columnspan=2)

    result_label = tk.Label(root, text="")
    result_label.grid(row=4, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    add_expense_gui()
