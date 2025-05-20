monthly_income = int(input('Enter your monthly income: '))
monthly_expenses = int(input('Enter your monthly expenses: '))
monthly_savings = monthly_income - monthly_expenses
currency = '$'
annual_interest_rate = 0.05
Projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)
print(f'Your monthly savings is: {currency}{monthly_savings}')
print(f'Your projected savings after one year,with interest, is: {currency}{Projected_savings}')