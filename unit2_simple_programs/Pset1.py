# Paste your code into this box
def creditRemainingBalance(balance, annualInterestRate, monthlyPaymentRate):

    monthlyInterestRate = annualInterestRate / 12.0

    for month in range(1, 13):
        # first we calculate Minimum monthly payment
        monthlyPayment = monthlyPaymentRate * balance

        # remove the monthlyPayment
        balance -= monthlyPayment

        # calculate interest on this balance
        monthlyInterest = monthlyInterestRate * balance

        # add the interest for this month to the balance
        balance += monthlyInterest

        # print(f"Month {month} Remaining balance {balance:.2f}")
        
    return balance

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

remainingBalance = creditRemainingBalance(balance, annualInterestRate, monthlyPaymentRate)
remainingBalance = round(remainingBalance, 2)

print("Remaining balance:", remainingBalance)