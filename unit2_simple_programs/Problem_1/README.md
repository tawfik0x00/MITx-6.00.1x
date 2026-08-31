# Problem 1 - Paying Debt Off in a Year (Minimum Monthly Payment)

## Problem Statement

Write a program to calculate the remaining credit card balance after one year, given that the cardholder pays only the minimum monthly payment each month.

**Given variables:**
- `balance` — the outstanding balance
- `annualInterestRate` — annual interest rate as a decimal
- `monthlyPaymentRate` — minimum monthly payment rate as a decimal

**Formula per month:**
```
Monthly interest rate   = annualInterestRate / 12.0
Minimum monthly payment = monthlyPaymentRate * balance
Monthly unpaid balance  = balance - minimum monthly payment
Updated balance         = monthly unpaid balance + (monthly interest rate * monthly unpaid balance)
```

**Example output:**
```
Remaining balance: 31.38
```

## Approach

Encapsulate the 12-month simulation in a function. Each iteration applies the payment and then compounds interest on the remaining unpaid balance. After 12 months, round the result to two decimal places and print.

**Concepts practiced:**
- Loops and arithmetic
- Function definition and return values
- Floating-point rounding
