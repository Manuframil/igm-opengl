import numpy as np
from triangle import Triangle

class TriangleStrip():
	def __init__(self, vertex, color, diffuse_c=.75, specular_c=.5, reflection=.25):
		self.vertex = np.array(vertex)
		self.create_triangles(color, diffuse_c=.75, specular_c=.5, reflection=.25)

	def create_triangles(self, color, diffuse_c=.75, specular_c=.5, reflection=.25):
		size = len(self.vertex) - 2
		self.triangles = np.empty(size, dtype=Triangle)
		v1,v3 = 0,2
		while v3 < len(self.vertex):
			self.triangles[v1] = Triangle(self.vertex[v1:v3+1], color, diffuse_c, specular_c, reflection)
			v1 += 1
			v3 += 1

	def get_strip(self):
		return self.triangles