import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Critical_Thinking.csv")

# Clean the 'Reason_For_Using_ChatGPT' column
df['Reason_For_Using_ChatGPT'] = df['Reason_For_Using_ChatGPT'].str.lower().str.strip()

# Standardization (group similar phrases)
df['Reason_For_Using_ChatGPT'] = df['Reason_For_Using_ChatGPT'].replace({
    'no idea': 'unsure',
    'saves time': 'saves time',
    'better answers': 'better answers'
})

# Group by reason and calculate average aptitude
reason_avg = df.groupby('Reason_For_Using_ChatGPT')['Aptitude_Score'].mean().sort_values(ascending=False)

# Display results
print("Average Aptitude Score by Reason for Using ChatGPT:")
print(reason_avg)

# Visualize
plt.figure(figsize=(8, 5))
reason_avg.plot(kind='bar', color='skyblue')
plt.title("Average Aptitude Score by Reason for Using ChatGPT")
plt.xlabel("Reason for Using ChatGPT")
plt.ylabel("Average Aptitude Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
