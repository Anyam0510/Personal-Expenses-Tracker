# 🧾 Personal Expense Tracker (Tkinter GUI + Multi-User Support)

This is a Python-based personal expense tracking application with a clean graphical interface built using `tkinter`. It supports **multiple users**, **persistent data storage**, and provides options to **add, edit, delete, and summarize expenses**.

---

## Features

- **Multi-User Authentication**
  - Each user logs in with a username
  - Personal expenses are stored in separate CSV files

- **Add New Expenses**
  - Record the amount, category (e.g., Food, Transport), and date
  - If no date is entered, today’s date is automatically used

- **Edit/Delete Expenses**
  - Modify or remove existing entries from the GUI

- **View Summary**
  - View total and category-wise expense breakdown

- **Data Persistence**
  - Each user’s data is saved to a local CSV file

---

## GUI Preview

> Built with `tkinter`, the interface is simple and user-friendly.  
> You’ll interact with dialog boxes and a summary dashboard via buttons.

---

## Project Structure

```

ExpenseTrackerGUI/
├── expense\_tracker\_gui.py             # Main Python script
├── sample\_user\_expenses.csv           # Example CSV data
└── user\_data/
└── {username}\_expenses.csv        # Auto-generated per user

````

---

## Requirements

- Python 3.x  
- No external libraries required (`tkinter` and `csv` are built-in)

---

## How to Run

1. Download or clone this repository:
    ```bash
    git clone https://github.com/your-username/ExpenseTrackerGUI.git
    cd ExpenseTrackerGUI
    ```

2. Run the application:
    ```bash
    python expense_tracker_gui.py
    ```

3. Enter a **username** to register or log in.

4. Use the buttons to:
    - Add an expense
    - View summaries
    - Edit or delete entries
    - Logout

---

## Sample Data

You can check the format of saved expenses in the file:  
[`sample_user_expenses.csv`](./sample_user_expenses.csv)

```csv
amount,category,date
150.0,Food,2025-07-25
70.0,Transport,2025-07-26
200.0,Entertainment,2025-07-26
50.0,Groceries,2025-07-27
````

---

## Future Enhancements

* Add expense visualizations with `matplotlib`
* Web-based version using Flask or Django
* Export reports to PDF
* Notifications for high spending

---

## Author

Developed by ANYAM ANITHA
anitha.anyam1016@gmai.com

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
