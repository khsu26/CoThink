import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Load dataset
df = pd.read_csv("Critical_Thinking.csv")

# Drop rows with missing data in the relevant columns
df = df.dropna(subset=["ChatGPT_Usage_Frequency_Per_Week", "Aptitude_Score"])

# Compute Pearson correlation
correlation, p_value = pearsonr(df["ChatGPT_Usage_Frequency_Per_Week"], df["Aptitude_Score"])
print(f"Correlation: {correlation:.2f}, P-value: {p_value:.4f}")

# Create a scatter plot with regression line
plt.figure(figsize=(8, 6))
sns.regplot(x="ChatGPT_Usage_Frequency_Per_Week", y="Aptitude_Score", data=df)
plt.title("ChatGPT Usage Frequency vs. Aptitude Score")
plt.xlabel("ChatGPT Usage Frequency (per week)")
plt.ylabel("Aptitude Score")
plt.grid(True)
plt.tight_layout()
plt.show()
