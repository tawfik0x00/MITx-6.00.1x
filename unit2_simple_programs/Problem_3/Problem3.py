def creditRemainingBalance(balance, annualInterestRate, fixedPayment):

    monthlyInterestRate = annualInterestRate / 12.0

    for month in range(1, 13):
        # remove the monthlyPayment
        MonthlyUnpaidBalance = balance - fixedPayment

        # add the interest for this month to the balance
        balance = MonthlyUnpaidBalance + (monthlyInterestRate * MonthlyUnpaidBalance)

        # print(f"Month {month} Remaining balance {balance:.2f}")
        
    return balance



# balance = 999999
# annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12.0


lower_bound = balance / 12
upper_bound = (balance * (1 + monthlyInterestRate)**12) / 12.0

epsilon = 0.01

original_balance = balance

while abs(upper_bound - lower_bound) > epsilon:
    # midpoint of the current bounds
    ans = (lower_bound + upper_bound) / 2

    remainingBalance = creditRemainingBalance(original_balance, annualInterestRate, ans)
   
    if remainingBalance > 0:
        lower_bound = ans
    else:
        upper_bound = ans

print("Lowest Payment:", round(ans, 2))








increment = 0.01