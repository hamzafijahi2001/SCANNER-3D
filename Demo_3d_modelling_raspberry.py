import numpy as np
from stl import mesh

R1 = [36, 3]
vertices = np.zeros(R1)
R2 = [36, 3]
faces = np.zeros(R2)



for i in range(36):
    vertices[i][0] = 10
    vertices[i][1] = 25



lines = []
with open('capturecalculation.txt') as f:
    lines = f.readlines()

fil = 0
for line in lines:
    if fil < 36:
        a = float(line[9:])
        vertices[fil][2] = a
        fil = fil + 1
    else:
        break


for l in range(0, 29, 2):  
    faces[l] = np.array([l, l + 1, l + 6])
    faces[l + 1] = np.array([l + 1, l + 6, l + 7])

objet2 = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
      if f[j]!=0:
        print(int(f[j]))
        objet2.vectors[i][j] = vertices[int(f[j]),:]
      else:
          np.delete(f, j)

objet2.save('objet2.stl')

from mpl_toolkits import mplot3d
from matplotlib import pyplot

# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

# Load the STL files and add the vectors to the plot
your_mesh = mesh.Mesh.from_file('objet2.stl')
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

# Auto scale to the mesh size
scale = your_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()