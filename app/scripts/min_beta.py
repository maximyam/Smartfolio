"""
Min Beta Portfolio Optimizer
----------------------------
This module provides functions to adjust the quantities of equities in a portfolio to minimize its beta while keeping the total value unchanged.

Functions:
1. `minimize_portfolio_beta`: Adjusts quantities to minimize the portfolio's beta.

Inputs:
- equities: A list of dictionaries, where each dictionary represents an equity and contains keys 'beta', 'qty', 'avg_price'. 

Outputs:
- A new list of equities with adjusted quantities that minimize the portfolio beta while maintaining the portfolio value.

Example:
equities = [
    {'beta': 1.2, 'qty': 100, 'avg_price': 50},
    {'beta': 0.9, 'qty': 150, 'avg_price': 30},
]
"""

from scipy.optimize import linprog


def minimize_portfolio_beta(equities):
    # Number of equities
    n = len(equities)

    # Coefficients for the objective function (we want to minimize beta)
    c = [equity['beta'] for equity in equities]

    # Coefficients for the equality constraint (total value remains unchanged)
    A_eq = [[equity['avg_price'] for equity in equities]]
    b_eq = [sum([equity['avg_price'] * equity['qty'] for equity in equities])]

    # Boundaries for equity quantities (they can't be negative)
    bounds = [(0, None) for _ in equities]

    # Linear programming to minimize portfolio beta
    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='simplex')

    # Assign the optimized quantities back to the equities
    for i, equity in enumerate(equities):
        equity['qty'] = round(res.x[i])

    return equities


# Example usage (commented out for export):
"""
equities = [
    {'beta': 1.2, 'qty': 100, 'avg_price': 50},
    {'beta': 0.9, 'qty': 150, 'avg_price': 30},
]

optimized_equities = minimize_portfolio_beta(equities)
for equity in optimized_equities:
    print(f"Equity with Beta {equity['beta']:.2f} has an adjusted quantity of {equity['qty']}")
"""
