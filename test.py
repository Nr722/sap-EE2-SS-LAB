import numpy as np
import matplotlib.pyplot as plt

# Generate values for the independent variable x
x = np.linspace(-4*np.pi, 4*np.pi, 100)  # Creating 100 points from 0 to 2*pi

# Calculate the dependent variable y = 2cos(x)
y=-np.arctan(0.8*np.sin(x)/(1-np.cos(x)))

# Create a plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = 2cos(x)', color='b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = 2cos(x)')
plt.grid(True)
plt.legend()
plt.show()
