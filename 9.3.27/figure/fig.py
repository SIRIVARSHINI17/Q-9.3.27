import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom, norm

# Parameters
n = 7  # Number of trials (shots)
p = 0.25  # Probability of hitting the target on a single shot

# Calculate the PMF for the binomial distribution
x = range(0, n + 1)  # Possible number of successful shots
pmf = [binom.pmf(k, n, p) for k in x]

# Parameters for the Gaussian distribution
mu = n * p  # Mean
sigma = np.sqrt(n * p * (1 - p))  # Standard deviation

# Generate a range of values for the x-axis
x_gaussian = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)

# Calculate the PDF for the Gaussian distribution
pdf = norm.pdf(x_gaussian, loc=mu, scale=sigma)

# Plot both PMF and PDF
plt.figure(figsize=(10, 5))
plt.stem(x, pmf, basefmt=' ', use_line_collection=True)
plt.plot(x_gaussian, pdf, label='Gaussian PDF', color='red')
plt.xlabel('Number of Successful Shots')
plt.ylabel('Probability / Probability Density')
plt.title('Binomial PMF vs. Gaussian PDF for Hitting the Target in 7 Shots')
plt.legend()
plt.grid(True)
plt.show()

