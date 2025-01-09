import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample DataFrame with test scores over time
data = {
    'Year': [2019, 2020, 2021, 2022, 2023],
    'Test_Score': [85, 88, 90, 93, 95]
}

df = pd.DataFrame(data)

# Plotting a line graph from the DataFrame
df.plot(kind='line', x='Year', y='Test_Score', marker='o', color='green')

# Adding title and labels
plt.title('Test Scores Over Years')
plt.xlabel('Year')
plt.ylabel('Test Score')

# Display the plot
plt.show()
