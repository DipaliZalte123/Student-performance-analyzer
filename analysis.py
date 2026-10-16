import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
df = pd.read_csv('data.csv')
print("--- Your Data ---")
print(df)

# Calculate average for each student
df['Average'] = df[['Maths','Science','English']].mean(axis=1)

# Find topper
topper = df.loc[df['Average'].idxmax()]
print(f"\nTopper is: {topper['Name']} with {topper['Average']:.1f}%")

# Subject averages
subject_avg = df[['Maths','Science','English']].mean()
print("\nSubject Average:")
print(subject_avg)

# Create Graph
subject_avg.plot(kind='bar', color=['skyblue','lightgreen','orange'])
plt.title('Subject Average Marks')
plt.ylabel('Marks')
plt.savefig('result_graph.png')

print("\nGraph saved as result_graph.png - Project SUCCESS!")