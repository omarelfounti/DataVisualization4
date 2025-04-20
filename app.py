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


#Exercise 2

from scipy.stats import ttest_ind, levene

# Sample data placeholder (replace with Excel data)
group1 = np.random.normal(100, 15, 30)
group2 = np.random.normal(110, 25, 30)

# Test for equal variances
stat, p_var = levene(group1, group2)
equal_var = p_var > 0.05  # if p > 0.05, variances are equal

# Independent t-test
t_stat, p_value = ttest_ind(group1, group2, equal_var=equal_var)

print("Equal variances:", equal_var)
print("t-statistic:", t_stat)
print("p-value:", p_value)
