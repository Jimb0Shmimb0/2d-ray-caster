import matplotlib.pyplot as plt

# Create figure and axis
fig, ax = plt.subplots()
print(type(ax))
print(type(0))

"""bound = Boundary(0,0,1,2,ax)
bound.draw()"""


# Set up the plot
ax.set_aspect('equal')
ax.set_xlim(-1, 3)
ax.set_ylim(-1, 3)
ax.axis('off')


ax.quiver(0, 0, 1, 1, angles='xy', scale_units='xy', scale=1, color='black')
ax.plot([2, 2], [-1, 3], color='black', linewidth=2)
plt.draw()

# Keep the window open
plt.show()
