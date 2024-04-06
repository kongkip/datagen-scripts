from datetime import datetime, timedelta
import random
import pandas as pd

# Parameters
start_date = datetime(2024, 4, 1)
end_date = datetime(2024, 4, 30)
income_days = [1, 15]  # Days of the month when income is received
monthly_income = [2000, 1500]  # Corresponding income amounts
expense_descriptions = [
    "Groceries", "Internet Bill", "Electricity Bill", "Coffee with friends",
    "Rent", "Gas", "Car Insurance", "Netflix Subscription", "Dinner Date",
    "Gym Membership", "Clothes", "Books", "Public Transport", "Phone Bill",
    "Health Insurance", "Dental Checkup", "Gift", "Charity", "Savings Deposit"
]

# Function to generate dataset
def generate_monthly_budget_dataset(start_date, end_date, income_days, monthly_income, expense_descriptions):
    current_date = start_date
    data = []

    while current_date <= end_date:
        # Income
        if current_date.day in income_days:
            income_index = income_days.index(current_date.day)
            data.append([current_date.date(), monthly_income[income_index], '', 'Salary'])
        
        # Expenses
        num_expenses_today = random.randint(1, 3)  # Random number of expenses for the day
        for _ in range(num_expenses_today):
            description = random.choice(expense_descriptions)
            expense_amount = random.randint(10, 500)  # Random expense amount
            data.append([current_date.date(), '', expense_amount, description])
        
        current_date += timedelta(days=1)
    
    return data

# Generate dataset
monthly_budget_dataset = generate_monthly_budget_dataset(start_date, end_date, income_days, monthly_income, expense_descriptions)


# Convert dataset to DataFrame
df = pd.DataFrame(monthly_budget_dataset, columns=['Date', 'Income', 'Expense', 'Description'])
df.to_csv('personal_monthly_budget.csv', index=False)