import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("AI_Student.csv")
df2 = df.drop(columns=["SessionID", "SessionDate"], inplace = False)
# inplace false = creating a copy of the dataframe

# Group by TaskType and calculate average satisfaction
task_satisfaction = df.groupby('TaskType')['SatisfactionRating'].mean().reset_index()

# Sort from highest to lowest
ranked = task_satisfaction.sort_values(by='SatisfactionRating', ascending=False)

# Print the result
print(ranked.to_string(index=False))

# Plotting
plt.figure(figsize=(8, 5))
plt.bar(ranked['TaskType'], ranked['SatisfactionRating'] - 3)

# Labeling
plt.xlabel("Task Type")
plt.ylabel("Average Satisfaction Rating")
plt.title("Average Satisfaction by Task Type (minus 3)")
plt.ylim(0, 1)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.xticks(rotation=45)

# Show chart
plt.tight_layout()
plt.show()
