import numpy as np
from scipy.stats import norm

# Parameters
n_trials = 7
p_success = 0.25
mean = n_trials * p_success
std_dev = np.sqrt(n_trials * p_success * (1 - p_success))

# Calculate the Z-score for X = 1
x = 1
z = (x - mean) / std_dev

# Calculate the probability of X being at least 1
probability = 1 - norm.cdf(z)

print(f"The probability of hitting the target at least twice is approximately {probability:.4f}")

