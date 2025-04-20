import pandas as pd
from scipy.stats import f_oneway

# Load the data
file_path = "anova2.xlsx"  
data = pd.read_excel(file_path)

# Separate the groups
group_A = data[data['system'] == 'A']['time']
group_B = data[data['system'] == 'B']['time']
group_C = data[data['system'] == 'C']['time']

# Perform One-way ANOVA
f_stat, p_value = f_oneway(group_A, group_B, group_C)

print("One-way ANOVA Results:")
print(f"F-statistic: {f_stat:.4f}")
print(f"p-value: {p_value:.6f}")

# Interpretation
alpha = 0.01
if p_value < alpha:
    print("Conclusion: Reject the null hypothesis.")
    print("There is a statistically significant difference in response times among the systems.")
else:
    print("Conclusion: Fail to reject the null hypothesis.")
    print("No significant difference in response times among the systems.")