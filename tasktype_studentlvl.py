import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("AI_Student.csv")
df2 = df.drop(columns=["SessionID", "SessionDate"], inplace = False)
# inplace false = creating a copy of the dataframe

# Group by StudentLevel and TaskType, count how many times each task was used
task_counts = df2.groupby(['StudentLevel', 'TaskType']).size().reset_index(name='Count')

# Sort the counts within each student level from highest to lowest
ranked = task_counts.sort_values(['StudentLevel', 'Count'], ascending=[True, False])

# Print the result
print(ranked.to_string(index=False))

# Create the grouped bar chart
plt.figure(figsize=(10, 6))
sns.barplot(data=task_counts, x='TaskType', y='Count', hue='StudentLevel')

# Add labels and title
plt.title("AI Task Types Used by Student Level")
plt.xlabel("Task Type")
plt.ylabel("Number of Sessions")
plt.legend(title="Student Level")
plt.tight_layout()
plt.show()
