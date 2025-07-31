'''
collects data for use in `main.py`
'''


from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I":"Income","E":"Expense"}

def get_date(prompt, allow_default=False):
  date_str = input(prompt)
  if allow_default and not date_str: #if the user doesn't enter input
    return datetime.today().strftime()

  try:
    valid_date = datetime.strptime(date_str, date_format)
    return valid_date.strftime(date_format) #cleans up date into proper format
  except ValueError:
    print("Invalid date format. Please enter the date in DD-MM-YYYY format.")
    return get_date(prompt, allow_default) #returns to function until `valid_date` passes


def get_amount():
  try:
    amount = float(input("Enter the amount: "))
    if amount <= 0:
      raise ValueError("Amount must be non-negative AND non-zero.")
    return amount
  except ValueError as e:
    print(e)
    return get_amount()

def get_category():
  category = input("Enter the category (I for Income, E for Expense): ")
  if category not in CATEGORIES:
    print("Invalid input.")
    return get_category()

  return CATEGORIES(category) #returns "category" value in CATEGORIES dictionary

def get_description():
  return input("Enter a brief description: ") #description is optional, so it can return None or return the entered input