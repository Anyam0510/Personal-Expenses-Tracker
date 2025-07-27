
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import csv
import os
from datetime import datetime
from collections import defaultdict

DATA_FOLDER = "sample_user_expenses"

if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker")
        self.username = None
        self.expenses = []
        self.file_path = None

        self.login_screen()

    def login_screen(self):
        self.clear_window()

        tk.Label(self.root, text="Login / Register", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Username").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)

    def login(self):
        username = self.username_entry.get().strip()
        if username:
            self.username = username
            self.file_path = os.path.join(DATA_FOLDER, f"{self.username}_expenses.csv")
            self.load_expenses()
            self.main_screen()
        else:
            messagebox.showerror("Error", "Username cannot be empty.")

    def load_expenses(self):
        self.expenses.clear()
        if os.path.exists(self.file_path):
            with open(self.file_path, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.expenses.append({
                        "amount": float(row["amount"]),
                        "category": row["category"],
                        "date": row["date"]
                    })

    def save_expenses(self):
        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["amount", "category", "date"])
            writer.writeheader()
            writer.writerows(self.expenses)

    def main_screen(self):
        self.clear_window()

        tk.Label(self.root, text=f"Welcome, {self.username}", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Add Expense", width=25, command=self.add_expense).pack(pady=5)
        tk.Button(self.root, text="View Summary", width=25, command=self.view_summary).pack(pady=5)
        tk.Button(self.root, text="Edit/Delete Expense", width=25, command=self.edit_delete_expense).pack(pady=5)
        tk.Button(self.root, text="Logout", width=25, command=self.login_screen).pack(pady=10)

    def add_expense(self):
        try:
            amount = float(simpledialog.askstring("Amount", "Enter amount: ₹"))
            category = simpledialog.askstring("Category", "Enter category (e.g. Food, Transport):")
            date_input = simpledialog.askstring("Date", "Enter date (YYYY-MM-DD) or leave blank for today:")
            date = date_input if date_input else datetime.today().strftime('%Y-%m-%d')
            self.expenses.append({"amount": amount, "category": category, "date": date})
            self.save_expenses()
            messagebox.showinfo("Success", "Expense added!")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def view_summary(self):
        total = sum(e["amount"] for e in self.expenses)
        category_summary = defaultdict(float)
        for e in self.expenses:
            category_summary[e["category"]] += e["amount"]

        summary_text = f"Total Spending: ₹{total:.2f}\n\n"
        summary_text += "Spending by Category:\n"
        for cat, amt in category_summary.items():
            summary_text += f"{cat}: ₹{amt:.2f}\n"

        messagebox.showinfo("Summary", summary_text)

    def edit_delete_expense(self):
        self.clear_window()
        tk.Label(self.root, text="Edit or Delete Expenses", font=("Arial", 16)).pack(pady=10)

        tree = ttk.Treeview(self.root, columns=("Amount", "Category", "Date"), show="headings")
        tree.heading("Amount", text="Amount")
        tree.heading("Category", text="Category")
        tree.heading("Date", text="Date")
        tree.pack(pady=10)

        for i, exp in enumerate(self.expenses):
            tree.insert('', 'end', iid=i, values=(exp["amount"], exp["category"], exp["date"]))

        def delete_selected():
            selected = tree.selection()
            if selected:
                for item in selected:
                    del self.expenses[int(item)]
                self.save_expenses()
                self.edit_delete_expense()
            else:
                messagebox.showerror("Error", "No item selected.")

        def edit_selected():
            selected = tree.selection()
            if selected:
                idx = int(selected[0])
                exp = self.expenses[idx]
                new_amount = float(simpledialog.askstring("Edit Amount", "Enter new amount:", initialvalue=exp["amount"]))
                new_category = simpledialog.askstring("Edit Category", "Enter new category:", initialvalue=exp["category"])
                new_date = simpledialog.askstring("Edit Date", "Enter new date:", initialvalue=exp["date"])
                self.expenses[idx] = {"amount": new_amount, "category": new_category, "date": new_date}
                self.save_expenses()
                self.edit_delete_expense()
            else:
                messagebox.showerror("Error", "No item selected.")

        tk.Button(self.root, text="Edit Selected", command=edit_selected).pack(pady=5)
        tk.Button(self.root, text="Delete Selected", command=delete_selected).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_screen).pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.geometry("400x500")
    root.mainloop()
