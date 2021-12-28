import numpy as np
import util
from figure import Figure

class Sphere(Figure):
	def __init__(self, position, radius, color, diffuse_c=1.0, specular_c=1.0,reflection = .5):
		self.radius = radius
		super().__init__(np.array(position), np.array(color), diffuse_c, specular_c, reflection)

	def intersect(self, O, D):
		a = np.dot(D, D)
		OS = O - self.position
		b = 2 * np.dot(D, OS)
		c = np.dot(OS, OS) - self.radius ** 2
		disc = b * b - 4 * a * c
		if disc > 0:
			distSqrt = np.sqrt(disc)
			q = (-b - distSqrt) / 2.0 if b < 0 else (-b + distSqrt) / 2.0
			t0 = q / a
			t1 = c / q
			t0, t1 = min(t0, t1), max(t0, t1)
			if t1 >= 0:
				return t1 if t0 < 0 else t0
		return np.inf

	def get_normal(self, M):
		return util.normalize(M - self.position)