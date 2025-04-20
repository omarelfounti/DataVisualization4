import pandas as pd
from scipy.stats import mannwhitneyu

# -----------------------
# Exercise 1: Reaction Time vs Age
# -----------------------
age_20 = [4.22, 5.13, 1.80, 3.34, 2.72, 2.80, 4.33, 3.60]
age_50 = [5.42, 3.39, 2.55, 4.45, 5.55, 4.96, 5.88, 6.30, 5.10]

u_stat1, p_value1 = mannwhitneyu(age_20, age_50, alternative='two-sided')

print("Exercise 1: Reaction Time vs Age")
print(f"U-statistic: {u_stat1}")
print(f"p-value: {p_value1:.4f}")
if p_value1 < 0.05:
    print("Conclusion: Reaction time is age dependent.\n")
else:
    print("Conclusion: No significant difference in reaction time by age.\n")

# -----------------------
# Exercise 2: Satisfaction with Management by Gender
# -----------------------
# Load data from Excel file
df = pd.read_excel("mann1.xlsx")

# Split by gender
male_scores = df[df['gender'] == 'male']['manag']
female_scores = df[df['gender'] == 'female']['manag']

# Mann-Whitney U test
u_stat2, p_value2 = mannwhitneyu(male_scores, female_scores, alternative='two-sided')

print("Exercise 2: Management Satisfaction by Gender")
print(f"U-statistic: {u_stat2}")
print(f"p-value: {p_value2:.4f}")
if p_value2 < 0.05:
    print("Conclusion: Significant difference in satisfaction with management between genders.")
else:
    print("Conclusion: No significant difference between genders.")