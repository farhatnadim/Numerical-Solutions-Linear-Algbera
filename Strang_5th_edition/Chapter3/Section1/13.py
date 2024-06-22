import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Create a new figure
fig = plt.figure()

# Add a 3D axes to the figure
ax = fig.add_subplot(111, projection='3d')

# Create a plane
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = (X+Y -4)/2 # plane equation 
N =  np.array([1,1,-2])

V1 = np.array([4,0,0]) # V = sum of two vectors belonging to the plane]
V2 = np.array([0,4,0])
print(f"V1 in plane {np.dot(N,V1) == 0}")
print(f"V2 in plane {np.dot(N,V2) == 0}")
print(f"V3 in plane {np.dot(N,(V2-V1)) == 0}")
#V2 = np.array([0,-2,-1])
#V3 = V1+V2
O = np.array([0,0,0])
# Fill the plane with a color
ax.plot_surface(X, Y, Z, color='red',alpha=0.5)
ax.quiver(0, 0, 0, N[0], N[1], N[2], color='green')
#ax.quiver(0, 0, 0, V2[0], V2[1], V2[2], color='blue')
#ax.quiver(0, 0, 0, V3[0], V3[1], V3[2], color='black')

# Set the axes labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()