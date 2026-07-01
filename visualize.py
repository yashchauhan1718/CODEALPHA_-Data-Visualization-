import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('all_quotes.csv')

author_counts = df['Author'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=author_counts.values, y=author_counts.index, palette='viridis')

plt.title('Top Authors by Number of Quotes')
plt.xlabel('Number of Quotes')
plt.ylabel('Author Name')

plt.savefig('top_authors_chart.png')
print("Task 3 completed: 'top_authors_chart.png' has been saved.")