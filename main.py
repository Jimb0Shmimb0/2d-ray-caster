import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Create figure and axes
fig, ax = plt.subplots()

# Define vector components (U, V)
U = [1, 0, -1]
V = [0, 1, -1]

# Create matching origins for each vector
X = [0, 0, 0]  # x-coordinates of origins
Y = [0, 0, 0]  # y-coordinates of origins

# Plot vectors
ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, color='green')

# Add a circle with no fill
circle = patches.Circle((0, 0), radius=1.5, fill=False, edgecolor='blue', linewidth=2)
ax.add_patch(circle)

# Remove axes, labels, grid, and everything else
ax.set_axis_off()

# Set limits and aspect
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')

# Show plot
plt.show()
