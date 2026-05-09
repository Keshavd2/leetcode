import pandas as pd
from scipy.stats import chi2_contingency

# Load ACS dataset
df = pd.read_csv('/Users/keshavdhamanwala/Downloads/ACS.csv')  # Replace with your actual file path

# Step 1: Create contingency table
# Fill missing combinations with 0 to avoid NaN
contingency_table = pd.crosstab(df['Married'], df['USCitizen'], dropna=False)
contingency_table = contingency_table.fillna(0)
print("Contingency Table:")
print(contingency_table)

# Step 2: Perform Chi-square test of independence
chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)

# Step 3: Print results
print(f"\nChi-square statistic: {chi2_stat:.3f}")
print(f"Degrees of freedom: {dof}")
print(f"P-value: {p_value:.3f}")

print("\nExpected counts under independence:")
print(pd.DataFrame(expected, index=contingency_table.index, columns=contingency_table.columns))








