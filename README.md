# AIML-Project

Expense Tracker
Name: Shlok Pratap Singh
Registration No.: 25BAI10668
Subject: Fundamentals in AI and ML
About
The Expense Tracker lets one manage their spending directly from the terminal. All data is stored in a MySQL database, so our records are never lost between sessions. The interface is simple and menu-driven.
Features
1. Add new expense records (date, category, amount, payment mode)
2. View all expenses in a clean formatted grid table
3. Delete any expense record by its ID
4. Update any field of an existing record
5. Search expenses by category
6. Calculate total expenditure across all records

Steps:

1. Enter your MySQL root password when prompted.

2. The program will automatically:
   - Create the ‘expense_tracker’ database if it doesn't exist
   - Create the ‘Expenses’ table if it doesn't exist
   - Connect and launch the main menu
Function Description
checkdb(): Creates the ‘expense_tracker’ database if it doesn't already exist 
addexp(): Takes user input and inserts a new expense record into the DB 
remexp(): Deletes a record permanently using its ID
view_table(): Fetches and displays all records in a formatted grid 
upexp(): Updates a specific field of a record by ID
totalexp(): Uses sum() function to calculate and display total expenses 
sec(): Filters and displays records by a given category

______________________________________________________________________
Menu Options
1.	View expenses
2.	Add expense
3.	Remove expense
4.	Show total expenses
5.	Update expense
6.	Search by Category
7.	Exit
