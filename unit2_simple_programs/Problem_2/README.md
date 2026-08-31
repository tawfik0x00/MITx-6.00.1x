# Problem 2 - Minimum Fixed Monthly Payment

## Problem Statement

Write a program that finds the minimum fixed monthly payment (rounded to the nearest $10) required to pay off a credit card balance within 12 months.

Unlike Problem 1, the monthly payment here is a constant amount — not a percentage of the remaining balance.

**Given variables:**
- `balance` — the outstanding balance
- `annualInterestRate` — annual interest rate as a decimal

**Formula per month:**
```
Monthly interest rate  = annualInterestRate / 12.0
Monthly unpaid balance = balance - fixed payment
Updated balance        = monthly unpaid balance + (monthly interest rate * monthly unpaid balance)
```

**Example output:**
```
Lowest Payment: 310
```

## Approach

Use exhaustive enumeration starting at $10 and incrementing by $10 on each iteration. For each candidate payment, simulate the full 12-month repayment. Stop and print the first payment amount that results in a balance of zero or below.

**Concepts practiced:**
- Exhaustive enumeration (brute-force search)
- Simulating financial calculations with loops
- While loops with break conditions
