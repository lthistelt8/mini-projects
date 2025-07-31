'''
Executes business logic, using `data_entry.py` return values
'''

import matplotlib as plt
import pandas as pd
import csv
from datetime import datetime
from data_entry import get_category, get_amount, get_date, get_description, CATEGORIES

class CSV:
  CSV_FILE = "finance_data.csv" #class variable
  COLUMNS = ["date","amount","category","description"]
  FORMAT = "%d-%m-%Y"

  @classmethod #access class without accessing class instances (objects)
  def initialize_csv(cls):
    try:
      pd.read_csv(cls.CSV_FILE)
    except FileNotFoundError:
      df = pd.DataFrame(columns=cls.COLUMNS) #specifies column headings; DataFrame can access rows and columns
      df.to_csv(cls.CSV_FILE, index=False)

  @classmethod
  def add_entry(cls, date, amount, category, description):
    new_entry = {
      'date':date,
      'amount':amount,
      'category':category,
      'description':description
    }
    with open(cls.CSV_FILE,'a',newline="") as csvfile: #will handle closing the file, including dealing with any memory leaks
      writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS) #takes dictionary, writes into .csv file
      writer.writerow(new_entry) #writes a row, using the "new entry" parameters
    print("Entry added successfully!")

  @classmethod
  def get_transactions(cls, start_date, end_date):
    df = pd.read_csv(cls.CSV_FILE)
    df['date'] = pd.to_datetime(df['date'], format=CSV.FORMAT) #directly accesses 'date' column of CSV file, converts to a datetime object
    start_date = datetime.strptime(start_date, CSV.FORMAT) #converts start_date from str to datetime
    end_date = datetime.strptime(end_date, CSV.FORMAT)

    mask = (df['date']) >= start_date and (df['date']) <= end_date #filters by data in 'date' row (the "masked" data) greater than the start_date, less than the end_date, using data converted from strings
    filtered_df = df.loc[mask] #locates all instances where the data matches the mask

    if filtered_df.empty:
      print("No transactions in the given date range.")

    print(
      f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}"
      ) #displays all transactions within date range
    print(
      filtered_df.to_string(index=False, formatters = {'date': lambda x: x.strftime(CSV.FORMAT)}
      ) 
    )
    
    total_income = filtered_df[filtered_df['category'] == 'Income']['amount'].sum() #filters all rows with "Income" label, then totals the 'amount'
    total_expense = filtered_df[filtered_df['category'] == 'Expense']['amount'].sum()
    print("\nSummary")
    print(f"Total income: ${total_income:.2f}")
    print(f"Total expense: ${total_expense:.2f}")
    print(f"Net Savings: ${(total_income - total_expense):.2f}")

    return filtered_df

  def add():
    CSV.initialize_csv()
    date = get_date(
      "Enter date in DD-MM-YYYY format (or Enter to use current date): ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

def plot_transaction(df):
  df.set_index('date', inplace = True)

  income_df = df[df['category'] == 'Income'].resample('D').sum().reindex(df, index, fill_value=0) #'D': daily frequency, takes filtered df and adds row for all days, even empty days
  expense_df = df[df['category'] == 'Expense'].resample('D').sum().reindex(df, index, fill_value=0)

  plt.figure(figsize=(10, 5))
  plt.plot(income_df.index, income_df['amount'], label="Income",color="g")
  plt.plot(expense_df.index, expense_df['amount'], label="Expense",color="r")
  plt.xlabel("Date")
  plt.ylabel("'Amount")
  plt.title("Income + Expenses Over Time")
  plt.legend()
  plt.grid(True)
  plt.show()

def main():
  while True:
    print("\nHello! What would you like to do?")
    print("1. Add an income or expense")
    print("2. View transactions in a date range")
    print("3. Quit")

    choice = int(input("> "))

    if choice == 1:
      add()
    elif choice == 2:
      start_date = get_date("Enter the start date (dd-mm-yyyy): ") #input will be assigned to variable, which will be passed as a parameter
      end_date = get_date("Enter the end date (dd-mm-yyyyy): ")
      df = CSV.get_transactions(start_date, end_date)
      if input("Do you want to see a plot? (y/n) ").lower() == 'y':
        plot_transaction(df)
    elif choice == 3:
      print("See ya!")
      break
    
    else:
      print("Invalid choice, please select between 1-3.")
      return main()

if __name__ == '__main__': #protects code from running main() function as an import
  main()