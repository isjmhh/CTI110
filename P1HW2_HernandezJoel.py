# Joel Hernandez

 # 2/25/2024

 # P1HW2

 # For this assignment you will create a program that does some basic math on numbers that are entered.
 #program Pseudocode (logic) 

 
 #  Ask user to enter their budget
budget = float(input("Enter your budget: $"))

# Ask user to enter travel destination
destination = input("Enter your travel destination: ")

#  they will spend on gas
gas_expense = float(input("Enter the amount you will spend on gas?: $"))

# Ask user amount they will spend on accommodation
accommodation_expense = float(input("Enter the amount you will spend on accommodation/hotel: $"))

# Ask user amount they will spend on food
food_expense = float(input("Enter the amount you will spend on food: $"))

# Add expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Subtract expenses from budget
remaining_budget = budget - total_expenses

# Step 8: Display results
print(f"--------------Travel Expenses-----------------")
print(f"Location: {destination}")
print(f"Initial Budget: ${budget}")
print(f"Fuel: ${gas_expense}")
print(f"Accommodation: ${accommodation_expense}")
print(f"Food: ${food_expense}")
print(f"Total expenses: ${total_expenses}")
print(f"Remaining Balance: ${remaining_budget}")
