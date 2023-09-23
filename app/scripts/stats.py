"""
Portfolio Metrics Calculator
--------------------------
This module provides functions to calculate various portfolio metrics:

1. `calculate_portfolio_metrics`: Computes the portfolio's beta, alpha, and Sharpe ratio.
2. `expected_return_CAPM`: Calculates the expected return of an equity using the CAPM model.

Inputs:
- equities: A list of dictionaries, where each dictionary represents an equity and has keys 'beta', 'qty', 'avg_price', and 'return'.
- benchmark_return: The return of the benchmark, typically the S&P 500 return.
- risk_free_rate: The risk-free rate, typically represented by a short-term treasury bill rate.

Outputs:
- `calculate_portfolio_metrics`: Returns the portfolio beta, alpha, and Sharpe ratio.
- `expected_return_CAPM`: Returns the expected return of an equity based on CAPM.

Example:
equities = [
    {'beta': 1.2, 'qty': 100, 'avg_price': 50, 'return': 0.08},
    {'beta': 0.9, 'qty': 150, 'avg_price': 30, 'return': 0.06},
]
benchmark_return = 0.07  # SPY500 return
risk_free_rate = 0.02  # Typically can be a short-term treasury bill rate
"""


def calculate_portfolio_metrics(equities, benchmark_return, risk_free_rate):
    total_investment = sum([equity['qty'] * equity['avg_price']
                           for equity in equities])

    # Portfolio Beta
    portfolio_beta = sum([(equity['qty'] * equity['avg_price'] /
                         total_investment) * equity['beta'] for equity in equities])

    # Portfolio Expected Return
    portfolio_return = sum([(equity['qty'] * equity['avg_price'] /
                           total_investment) * equity['return'] for equity in equities])

    # Portfolio Alpha
    portfolio_alpha = portfolio_return - risk_free_rate - \
        portfolio_beta * (benchmark_return - risk_free_rate)

    # Portfolio Sharpe Ratio
    portfolio_std_dev = sum([(equity['qty'] * equity['avg_price'] / total_investment)
                            * equity['beta'] * (benchmark_return - risk_free_rate) for equity in equities])
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_std_dev

    return portfolio_beta, portfolio_alpha, sharpe_ratio


def expected_return_CAPM(risk_free_rate, beta, market_return):
    """Calculate the expected return for an equity using CAPM."""
    return risk_free_rate + beta * (market_return - risk_free_rate)


# Example usage (commented out for export):
"""
equities = [
    {'beta': 1.2, 'qty': 100, 'avg_price': 50, 'return': 0.08},
    {'beta': 0.9, 'qty': 150, 'avg_price': 30, 'return': 0.06},
]

benchmark_return = 0.07  # SPY500 return
risk_free_rate = 0.02  # Typically can be a short-term treasury bill rate

portfolio_beta, portfolio_alpha, sharpe_ratio = calculate_portfolio_metrics(equities, benchmark_return, risk_free_rate)
print(f"Portfolio Beta: {portfolio_beta:.4f}")
print(f"Portfolio Alpha: {portfolio_alpha:.4f}")
print(f"Portfolio Sharpe Ratio: {sharpe_ratio:.4f}")
"""
