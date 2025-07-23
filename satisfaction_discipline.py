import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("AI_Student.csv")
df2 = df.drop(columns=["SessionID", "SessionDate"], inplace = False)
# inplace false = creating a copy of the dataframe

# Group by StudentLevel and Discipline, then calculate the average SatisfactionRating
avg = df2.groupby(['Discipline'])['SatisfactionRating'].mean()
ranked = avg.sort_values(ascending = False)
print(ranked.to_string())

# Plotting the bar chart
plt.figure(figsize=(10, 6))  # Set the figure size

# Create the bar chart
plt.bar(ranked.index, ranked.values - 3)

# Add labels and title
plt.xlabel("Discipline")
plt.ylabel("Average Satisfaction Rating out of 5 (at 3)")
plt.title("Average AI Satisfaction Rating by Discipline")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the chart
plt.tight_layout()  # Prevent label cutoff
plt.show()
