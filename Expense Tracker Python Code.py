#EXPENSE TRACKER CODE

import time
from tabulate import tabulate
import mysql.connector
pw=str(input("Please enter your password: "))
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=pw,
    )
cursor=mydb.cursor()
db="expense_tracker"

#CHECKING IF THE DATABASE EXISTS ON SYSTEM
def checkdb():
    cursor.execute(f"Create database if not exists {db};")
    print(f"Database {db} located.")
checkdb()
cursor.close()
mydb.close()

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=pw,
    database=db)
if mydb.is_connected():
    print("Successfully connected to database.")

cursor=mydb.cursor()

table="""Create table if not exists Expenses(
ID integer primary key auto_increment,
Date datetime not null,
Category text not null,
Amount real not null,
Payment_mode text
);"""
cursor.execute(table)


#FUNCTION TO ADD RECORD
def addexp():
    date=str(input("Enter the date: "))
    category=str(input("Enter the category: "))
    amount=float(input("Enter the amount: "))
    pm=str(input("Enter payment mode: "))
    insquery="INSERT INTO Expenses (date,category,amount,payment_mode) VALUES (%s,%s,%s,%s)"
    inval=(date,category,amount,pm)
    cursor.execute(insquery,inval)
    print("Adding record...")
    time.sleep(2)
    print("Record added.")
    mydb.commit()
    user=input("Press any key to continue.")
    

#FUNCTION TO REMOVE RECORD
def remexp():
    idr=tuple(input("Enter the ID: "))
    dquery="Delete from Expenses where id=%s"
    cursor.execute(dquery,idr)
    print("Deleting record...")
    time.sleep(2)
    print("Record Deleted.")
    mydb.commit()
    user=input("Press any key to continue.")

def view_table():
    vquery = "SELECT * FROM expenses;"
    cursor.execute(vquery)
    vt = cursor.fetchall()
    if not vt:
        print("No records found.")
    else:
        print("Loading records...")
        time.sleep(2)
        headers = ["ID", "Date", "Category", "Amount", "Payment mode"]
        print(tabulate(vt, headers, tablefmt="grid", floatfmt=".0f"))
    input("Press any key to continue.")

#FUNCTION TO UPDATE RECORDS
def upexp():
    upset=str(input("Which field do you want to update?: "))
    setv=input("Enter new value: ")
    upid=int(input("Enter ID of the record to be updated: "))
    upquery = f"UPDATE expenses SET {upset} = %s WHERE ID = %s"
    cursor.execute(upquery, (setv, upid))
    print("Updating record...")
    time.sleep(2)
    print("Record updated.")
    mydb.commit()
    user=input("Press any key to continue.")

#FUNCTION TO CALCULATE TOTAL EXPENSES
def totalexp():
    cursor.execute("Select sum(Amount) from Expenses;")
    tt=cursor.fetchone()
    total=tt[0]
    print("The total expense is Rs.",total)
    user=input("Press any key to continue.")

#FUNCTION TO SEARCH BY CATEGORY
def sec():
    cat = input("Enter the category you wish to search for: ")  # input string normally
    query = "SELECT * FROM expenses WHERE category = %s"
    cursor.execute(query, (cat,))  # pass the variable as a single-element tuple
    res = cursor.fetchall()
    if not res:
        print("No records found.")
    else:
        print("Loading records...")
        time.sleep(2)
        headers = ["ID", "Date", "Category", "Amount", "Payment mode"]
        print(tabulate(res, headers, tablefmt="grid", floatfmt=".0f"))
    input("Press any key to continue.")

#MENU
while True:
    print("1. View expenses")
    print("2. Add expense")
    print("3. Remove expense")
    print("4. Show total expenses")
    print("5. Update expense")
    print("6. Search by Category")
    print("7. Exit")
    i1=int(input("Please make your selection: "))
    if i1==1:
        view_table()
    elif i1==2:
        addexp()
    elif i1==3:
        remexp()
    elif i1==4:
        totalexp()
    elif i1==5:
        upexp()
    elif i1==6:
        sec()
    elif i1==7:
        print("Closing...")
        time.sleep(3)
        print("Database closed.")
        break
    else:
        print("Please select from the given options.")
cursor.close()
mydb.close()
