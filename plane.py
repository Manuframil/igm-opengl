import numpy as np
from figure import Figure

class Plane(Figure):
	def __init__(self, position, normal, color, diffuse_c=.75, specular_c=.5, reflection=.25):
		self.normal = np.array(normal)
		super().__init__(position, color, diffuse_c, specular_c, reflection)

	def intersect(self, O, D):
		denom = np.dot(D, self.normal)
		if np.abs(denom) < 1e-6:
			return np.inf
		d = np.dot(self.position - O, self.normal) / denom
		if d < 0:
			return np.inf
		return d

	def get_normal(self, M):
		return self.normal
