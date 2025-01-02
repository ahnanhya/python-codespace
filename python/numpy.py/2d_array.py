import numpy as np

array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

sum_rows = np.sum(array_2d, axis=1)
sum_columns = np.sum(array_2d, axis=0)

print("2D Array:")
print(array_2d)
print("\nSum of Rows:", sum_rows)
print("Sum of Columns:", sum_columns)
