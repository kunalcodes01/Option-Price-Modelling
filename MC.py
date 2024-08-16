import numpy as np

def monte_carlo_option_pricing(S, K, T, r, sigma, num_simulations=10000, option_type='call'):

    z = np.random.standard_normal(num_simulations)
    
    # Calculate the stock price at maturity using the geometric Brownian motion model
    ST = S * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * z)
    
    # Calculate the payoff for call or put option
    if option_type == 'call':
        payoffs = np.maximum(ST - K, 0)
    elif option_type == 'put':
        payoffs = np.maximum(K - ST, 0)
    else:
        raise ValueError("Invalid option type. Choose 'call' or 'put'.")

    option_price = np.exp(-r * T) * np.mean(payoffs)
    
    return option_price

# Example usage:
S = 100  # Current stock price
K = 100  # Strike price
T = 1    # Time to maturity (1 year)
r = 0.05 # Risk-free interest rate (5%)
sigma = 0.2 # Volatility (20%)

# Monte Carlo simulation
call_price_mc = monte_carlo_option_pricing(S, K, T, r, sigma, num_simulations=10000, option_type='call')
put_price_mc = monte_carlo_option_pricing(S, K, T, r, sigma, num_simulations=10000, option_type='put')

print(f"Monte Carlo Call Option Price: {call_price_mc:.2f}")
print(f"Monte Carlo Put Option Price: {put_price_mc:.2f}")
