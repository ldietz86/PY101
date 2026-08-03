# Mortgage/Car Loan Calculator
def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        num = float(number_str)
        return num <= 0
    except ValueError:
        return True

def invalid_interest_rate(number_str):
    try:
        num = float(number_str)
        return num < 0
    except ValueError:
        return True

prompt("Enter the loan amount: ")
loan_amount = input()

while invalid_number(loan_amount):
    prompt("Please enter a positive number.")
    loan_amount = input()

loan_amount = float(loan_amount)

prompt("Enter the annual interest rate percentage: ")
annual_interest_rate = input()

while invalid_interest_rate(annual_interest_rate):
    prompt("Please enter a valid rate (0 or greater).")
    annual_interest_rate = input()

annual_interest_rate = float(annual_interest_rate)

prompt("Enter the loan duration in years: ")
total_loan_duration = input()

while invalid_number(total_loan_duration):
    prompt("Please enter a positive number.")
    total_loan_duration = input()

loan_duration_months = int(total_loan_duration) * 12

if annual_interest_rate == 0:
    monthly_payment = loan_amount / loan_duration_months
else:
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-loan_duration_months)))
    
prompt(f"Monthly payment: ${monthly_payment:.2f}")

