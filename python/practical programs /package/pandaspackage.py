import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Sample DataFrame:")
print(df)

# Basic DataFrame operations
print("\nSummary Statistics:")
print(df.describe(include='all'))

# Save DataFrame to a CSV file
df.to_csv('sample_data.csv', index=False)
print("\nDataFrame saved to 'sample_data.csv'")
