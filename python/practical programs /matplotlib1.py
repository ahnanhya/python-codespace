import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Creating a line plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Sample Data')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot using Matplotlib')
plt.legend()

# Display the plot
plt.show()
