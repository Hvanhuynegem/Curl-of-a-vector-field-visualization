# create a vector field of the form F(x,y,z) = (y^2-z^2)i + (2xz +3)j + (2xy-4z)k

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a meshgrid of the points in the x, y, z space
x = np.linspace(-1, 1, 10)
y = np.linspace(-1, 1, 10)
z = np.linspace(-1, 1, 10)
X, Y, Z = np.meshgrid(x, y, z)

# Calculate the curl components
CurlFx = np.zeros_like(X)  # Since the curl in x-direction is 0
CurlFy = -2*Z - 2*Y
CurlFz = 2*Z - 2*Y

# Create a new figure for the curl
fig_curl = plt.figure()
ax_curl = fig_curl.add_subplot(111, projection='3d')

# Plot the vector field with colors based on magnitude
# Color by magnitude
c = np.sqrt(CurlFx**2 + CurlFy**2)
# Flatten and normalize
c = (c.ravel() - c.min()) / c.ptp()
# Repeat for each body line and two head lines
c = np.concatenate((c, np.repeat(c, 2)))
# Colormap
c = plt.cm.hsv(c)
print(c)

# Plot the curl vector field
q_curl = ax_curl.quiver(X, Y, Z, CurlFx, CurlFy, CurlFz,colors=c, length=0.2, normalize=True)

# Set the labels
ax_curl.set_xlabel('X')
ax_curl.set_ylabel('Y')
ax_curl.set_zlabel('Z')

# Set the title for the curl vector field plot
ax_curl.set_title('Curl of Vector Field F(x,y,z)')

# Show the plot
plt.show()