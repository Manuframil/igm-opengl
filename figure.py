import numpy as np

class Figure():
	def __init__(self, position, color, diffuse_c=.75, specular_c=.5, reflection=.25):
		self.position = position
		self.color = color
		self.reflection = reflection
		self.diffuse_c = diffuse_c
		self.specular_c = specular_c

	def intersect(self, O, D):
		raise NotImplementedError("Implemented in subclases")

	def get_normal(self, M):
		raise NotImplementedError("Implemented in subclases")

	def get_color(self, M):
		color = self.color
		if not hasattr(color, '__len__'):
			color = color(M)
		return color
