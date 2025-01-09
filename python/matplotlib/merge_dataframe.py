import pandas as pd

# Creating the first DataFrame (students' information)
data1 = {
    'Student_ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [20, 21, 22, 23]
}
df1 = pd.DataFrame(data1)

# Creating the second DataFrame (students' scores)
data2 = {
    'Student_ID': [1, 2, 3, 4],
    'Subject': ['Math', 'Science', 'English', 'History'],
    'Score': [85, 92, 78, 88]
}
df2 = pd.DataFrame(data2)

# Merging the two DataFrames on 'Student_ID'
merged_df = pd.merge(df1, df2, on='Student_ID')

# Display the merged DataFrame
print(merged_df)
