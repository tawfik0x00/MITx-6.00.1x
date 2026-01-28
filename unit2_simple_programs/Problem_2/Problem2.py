# Paste your code into this box
def creditRemainingBalance(balance, annualInterestRate, fixedPayment):

    monthlyInterestRate = annualInterestRate / 12.0

    for month in range(1, 13):
        # remove the monthlyPayment
        MonthlyUnpaidBalance = balance - fixedPayment

        # add the interest for this month to the balance
        balance = MonthlyUnpaidBalance + (monthlyInterestRate * MonthlyUnpaidBalance)

        # print(f"Month {month} Remaining balance {balance:.2f}")
        
    return balance

balance = 3329
annualInterestRate = 0.2

# if remaining balance == 0 stop and print the fixedPayment
# exhuastive enumeration start with guessed value ?
guess = 10
original_balance = balance

while True:
    remaining_balance = creditRemainingBalance(original_balance, annualInterestRate, guess)

    if remaining_balance <= 0:
        break

    guess += 10
    



print("Loswest Payment:", guess)