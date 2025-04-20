#Exercise 1

from scipy.stats import ttest_1samp

# Sample parameters
sample_mean = 109
mu = 60  # population mean
s = 40
n = 32

# Reconstruct data from mean and std for testing (simulate data)
import numpy as np
np.random.seed(0)
sample_data = np.random.normal(loc=sample_mean, scale=s, size=n)

# One-sample t-test
t_stat, p_value = ttest_1samp(sample_data, popmean=mu)

print("t-statistic:", t_stat)
print("p-value:", p_value / 2 if t_stat > 0 else 1 - p_value / 2)  # one-tailed


