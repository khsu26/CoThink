import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Critical_Thinking.csv")

# Clean 'Reason_For_Using_ChatGPT'
df['Reason_For_Using_ChatGPT'] = df['Reason_For_Using_ChatGPT'].str.lower().str.strip()

# Standardize responses
df['Reason_For_Using_ChatGPT'] = df['Reason_For_Using_ChatGPT'].replace({
    'no idea': 'unsure',
    'better answers': 'better answers',
    'saves time': 'saves time'
})

# Count reasons
reason_counts = df['Reason_For_Using_ChatGPT'].value_counts()

# Print results
print("Most common reasons for using ChatGPT:")
print(reason_counts)

# Create pie chart
plt.figure(figsize=(6, 6))
plt.pie(reason_counts, labels=reason_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Reasons Students Use ChatGPT")
plt.axis('equal')
plt.show()
