import matplotlib.pyplot as plt
import numpy as np

# Generate random data points
x = np.random.rand(50)  # 50 random points for x-axis
y = np.random.rand(50)  # 50 random points for y-axis

# Create a scatter plot
plt.scatter(x, y, color='green', marker='o')

# Adding title and labels
plt.title('Random Data Points Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Display the plot
plt.show()
