"""
Sharpe Ratio Portfolio Optimizer
--------------------------------
This module provides functions to adjust the quantities of equities in a portfolio to maximize its Sharpe Ratio while keeping the total value unchanged.

Functions:
1. `maximize_sharpe_ratio`: Adjusts quantities to maximize the portfolio's Sharpe Ratio.

Inputs:
- equities: A list of dictionaries, where each dictionary represents an equity and contains keys 'beta', 'qty', 'avg_price', 'return'.
- benchmark_return: The return of the benchmark, typically the S&P 500 return.
- risk_free_rate: The risk-free rate, typically represented by a short-term treasury bill rate.

Outputs:
- A new list of equities with adjusted quantities that maximize the portfolio Sharpe Ratio while maintaining the portfolio value.

Example:
equities = [
    {'beta': 1.2, 'qty': 100, 'avg_price': 50, 'return': 0.08},
    {'beta': 0.9, 'qty': 150, 'avg_price': 30, 'return': 0.06},
]
"""

from scipy.optimize import linprog


def maximize_sharpe_ratio(equities, benchmark_return, risk_free_rate):
    n = len(equities)

    # Coefficients for the objective function (we want to maximize Sharpe Ratio, so we minimize negative Sharpe Ratio)
    c = [-((equity['return'] - risk_free_rate) / (equity['beta'] *
           (benchmark_return - risk_free_rate))) for equity in equities]

    # Coefficients for the equality constraint (total value remains unchanged)
    A_eq = [[equity['avg_price'] for equity in equities]]
    b_eq = [sum([equity['avg_price'] * equity['qty'] for equity in equities])]

    # Boundaries for equity quantities (they can't be negative)
    bounds = [(0, None) for _ in equities]

    # Linear programming to maximize Sharpe Ratio (minimize negative Sharpe Ratio)
    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='simplex')

    # Assign the optimized quantities back to the equities
    for i, equity in enumerate(equities):
        equity['qty'] = round(res.x[i])

    return equities


# Example usage (commented out for export):
"""
equities = [
    {'beta': 1.2, 'qty': 100, 'avg_price': 50, 'return': 0.08},
    {'beta': 0.9, 'qty': 150, 'avg_price': 30, 'return': 0.06},
]

benchmark_return = 0.07  # SPY500 return
risk_free_rate = 0.02  # Typically can be a short-term treasury bill rate

optimized_equities = maximize_sharpe_ratio(equities, benchmark_return, risk_free_rate)
for equity in optimized_equities:
    print(f"Equity with Return {equity['return']:.2f} has an adjusted quantity of {equity['qty']}")
"""
