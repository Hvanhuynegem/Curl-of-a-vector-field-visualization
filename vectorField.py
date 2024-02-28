# create a vector field of the form F(x,y,z) = (y^2-z^2)i + (2xz +3)j + (2xy-4z)k

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a meshgrid of the points in the x, y, z space
x = np.linspace(-1, 1, 10)
y = np.linspace(-1, 1, 10)
z = np.linspace(-1, 1, 10)
X, Y, Z = np.meshgrid(x, y, z)

# Define the vector field
Fx = Y**2 - Z**2
Fy = 2*X*Z + 3
Fz = 2*X*Y - 4*Z

# Create the figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vector field with colors based on magnitude
# Color by magnitude
c = np.sqrt(Fx**2 + Fy**2)
# Flatten and normalize
c = (c.ravel() - c.min()) / c.ptp()
# Repeat for each body line and two head lines
c = np.concatenate((c, np.repeat(c, 2)))
# Colormap
c = plt.cm.hsv(c)
print(c)

q = ax.quiver(X, Y, Z, Fx, Fy, Fz, colors=c, length=0.2, normalize=True)

# Set the labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the title
ax.set_title('Vector Field F(x,y,z) = (y^2-z^2)i + (2xz +3)j + (2xy-4z)k')

# Show the plot
plt.show()