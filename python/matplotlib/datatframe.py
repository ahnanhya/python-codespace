import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample DataFrame with student test scores across different subjects
data = {
    'Subject': ['Math', 'Science', 'English', 'History', 'Art'],
    'Score': [85, 92, 78, 88, 91]
}

df = pd.DataFrame(data)

# Plotting a bar chart from the DataFrame
df.plot(kind='bar', x='Subject', y='Score', color='skyblue', legend=False)

# Adding title and labels
plt.title('Student Test Scores by Subject')
plt.xlabel('Subject')
plt.ylabel('Score')

# Display the plot
plt.show()
