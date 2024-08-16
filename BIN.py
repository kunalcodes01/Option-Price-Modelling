import numpy as np

def binomial_option_pricing(S, K, T, r, sigma, N, option_type='call', american=False):

    dt = T / N

    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    
    p = (np.exp(r * dt) - d) / (u - d)
    
    # Initialize asset prices at maturity
    ST = np.zeros(N + 1)
    for i in range(N + 1):
        ST[i] = S * (u ** (N - i)) * (d ** i)
    
    # Initialize option values at maturity
    if option_type == 'call':
        option_values = np.maximum(ST - K, 0)
    elif option_type == 'put':
        option_values = np.maximum(K - ST, 0)
    else:
        raise ValueError("Invalid option type. Choose 'call' or 'put'.")
    
    # Backward induction to calculate option price at t=0
    for j in range(N - 1, -1, -1):
        for i in range(j + 1):
            option_values[i] = np.exp(-r * dt) * (p * option_values[i] + (1 - p) * option_values[i + 1])
            if american:
                ST = S * (u ** (j - i)) * (d ** i)
                if option_type == 'call':
                    option_values[i] = max(option_values[i], ST - K)
                elif option_type == 'put':
                    option_values[i] = max(option_values[i], K - ST)
    
    return option_values[0]

# Example usage:
S = 100  # Current stock price
K = 100  # Strike price
T = 1    # Time to maturity (1 year)
r = 0.05 # Risk-free interest rate (5%)
sigma = 0.2 # Volatility (20%)
N = 100  # Number of time steps

# Binomial model
call_price_binom = binomial_option_pricing(S, K, T, r, sigma, N, option_type='call', american=False)
put_price_binom = binomial_option_pricing(S, K, T, r, sigma, N, option_type='put', american=False)

print(f"Binomial Model European Call Option Price: {call_price_binom:.2f}")
print(f"Binomial Model European Put Option Price: {put_price_binom:.2f}")

# American option pricing (if needed)
call_price_american = binomial_option_pricing(S, K, T, r, sigma, N, option_type='call', american=True)
put_price_american = binomial_option_pricing(S, K, T, r, sigma, N, option_type='put', american=True)

print(f"Binomial Model American Call Option Price: {call_price_american:.2f}")
print(f"Binomial Model American Put Option Price: {put_price_american:.2f}")
