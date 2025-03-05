import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Sine Wave', color='b', linestyle='--', marker='o')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Wave using Matplotlib')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
