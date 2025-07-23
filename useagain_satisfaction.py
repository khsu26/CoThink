import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("AI_Student.csv")
df2 = df.drop(columns=["SessionID", "SessionDate"], inplace = False)
# inplace false = creating a copy of the dataframe

# Group by UsedAgain and calculate average satisfaction
avg_satisfaction = df2.groupby('UsedAgain')['SatisfactionRating'].mean().reset_index()

# Print results
print(avg_satisfaction)

# Plotting
plt.figure(figsize=(6, 4))
plt.bar(avg_satisfaction['UsedAgain'].astype(str), avg_satisfaction['SatisfactionRating'], color=['red', 'green'])

# Labels and title
plt.xlabel("Used AI Again")
plt.ylabel("Average Satisfaction Rating")
plt.title("Satisfaction vs. Whether AI Was Used Again")
plt.ylim(0, 5)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Show plot
plt.tight_layout()
plt.show()
