import matplotlib.pyplot as plt
import numpy as np

# Generate data points for the x-axis (from 0 to 2π with a small step)
x = np.linspace(0, 2 * np.pi, 500)

# Calculate sine and cosine values for each point in x
y_sine = np.sin(x)
y_cosine = np.cos(x)

# Create the plot
plt.plot(x, y_sine, label='Sine', color='blue')    # Sine wave
plt.plot(x, y_cosine, label='Cosine', color='red')  # Cosine wave

# Add a title and labels
plt.title('Sine and Cosine Waves')
plt.xlabel('x (radians)')
plt.ylabel('y')

# Add a legend to differentiate between the sine and cosine waves
plt.legend()

# Display the plot
plt.grid(True)  # Adds a grid for better readability
plt.show()
