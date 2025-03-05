import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Salary': [70000, 80000, 90000, 100000]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Sample DataFrame:")
print(df)

# Basic DataFrame operations
print("\nSummary Statistics:")
print(df.describe(include='all'))

# Filtering data
filtered_df = df[df['Age'] > 30]
print("\nFiltered DataFrame (Age > 30):")
print(filtered_df)

# Save DataFrame to a CSV file
df.to_csv('sample_data.csv', index=False)
print("\nDataFrame saved to 'sample_data.csv'")
