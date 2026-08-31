# Problem 3 - Bisection Search for Minimum Payment

## Problem Statement

Improve upon Problem 2 by using bisection search to find the minimum fixed monthly payment to the nearest cent, without being constrained to multiples of $10. The bisection search approach is dramatically faster for large balances.

**Given variables:**
- `balance` — the outstanding balance
- `annualInterestRate` — annual interest rate as a decimal

**Search bounds:**
```
Monthly interest rate       = annualInterestRate / 12.0
Monthly payment lower bound = balance / 12
Monthly payment upper bound = (balance * (1 + monthly interest rate)^12) / 12.0
```

**Example output:**
```
Lowest Payment: 310.00
```

## Approach

Use bisection search within the computed bounds. At each step, test the midpoint of the current bounds by simulating 12 months of payments. If the remaining balance is positive, the payment is too low — raise the lower bound. If negative or zero, the payment is sufficient — lower the upper bound. Continue until the bounds converge within an epsilon of $0.01.

**Concepts practiced:**
- Bisection search (binary search on a continuous range)
- Algorithm efficiency compared to exhaustive enumeration
- Floating-point convergence and epsilon tolerance
