import matplotlib.pyplot as plt

# Data for the distribution of grades
grades = ['A', 'B', 'C', 'D']
distribution = [40, 30, 20, 10]  # Percentage distribution for each grade

# Create a pie chart
plt.pie(distribution, labels=grades, autopct='%1.1f%%', startangle=90, colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen'])

# Add a title
plt.title('Grade Distribution in the Class')

# Display the chart
plt.show()
