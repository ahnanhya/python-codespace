import matplotlib.pyplot as plt
import numpy as np

# Sample test scores for students
test_scores = [85, 90, 78, 92, 88, 76, 95, 89, 73, 91,
               84, 77, 80, 86, 93, 70, 79, 82, 87, 75]

# Create the histogram
plt.hist(test_scores, bins=8, color='skyblue', edgecolor='black')

# Adding title and labels
plt.title('Distribution of Test Scores')
plt.xlabel('Test Scores')
plt.ylabel('Number of Students')

# Display the histogram
plt.show()
