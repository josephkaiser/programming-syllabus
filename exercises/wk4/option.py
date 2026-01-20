'''
Monte Carlo, Black-Scholes Option pricing calculator
'''
import pdb
import random
import math

pdb.set_trace()
def european_option_mc(
    S0,     # initial stock price
    K,      # strike price
    T,      # time to maturity (years)
    r,      # risk-free rate
    sigma,  # volatility
    n_paths=100000,
    option_type="call"
):
    payoff_sum = 0.0

    for _ in range(n_paths):
        # Standard normal random variable
        Z = random.gauss(0.0, 1.0)

        # Terminal stock price under Black–Scholes
        ST = S0 * math.exp(
            (r - 0.5 * sigma**2) * T + sigma * math.sqrt(T) * Z
        )

        if option_type == "call":
            payoff = max(ST - K, 0.0)
        elif option_type == "put":
            payoff = max(K - ST, 0.0)
        else:
            raise ValueError("option_type must be 'call' or 'put'")

        payoff_sum += payoff

    # Discounted expected payoff
    price = math.exp(-r * T) * (payoff_sum / n_paths)
    return price

def implied_volatility_mc(
    market_price,
    S0,
    K,
    T,
    r,
    option_type="call",
    n_paths=5, # Try small n for initial bisection, then use rapidly converging method like N-R
    tol=1e-4,
    max_iter=50
):
    # Volatility bounds
    vol_low = 1e-4
    vol_high = 3.0

    for _ in range(max_iter):
        vol_mid = 0.5 * (vol_low + vol_high)

        price_mid = european_option_mc(
            S0, K, T, r, vol_mid, n_paths, option_type
        )

        if abs(price_mid - market_price) < tol:
            return vol_mid

        if price_mid > market_price:
            vol_high = vol_mid
        else:
            vol_low = vol_mid

    return vol_mid

S0 = 20.77
K = 23.00
T = 736
r = 0.0315
true_sigma = 0.341

# S0, K, T, r, true_sigma = 100, 110, 765, .04, 0.20

# Generate a "market price"
market_call = european_option_mc(
    S0, K, T, r, true_sigma, option_type="call"
)

iv = implied_volatility_mc(
    market_call, S0, K, T, r, option_type="call"
)

print("Market price:", market_call)
print("Implied vol :", iv)
