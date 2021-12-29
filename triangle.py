import numpy as np
from figure import Figure
from util import normalize

class Triangle(Figure):
	def __init__(self, vertex, color, diffuse_c=.75, specular_c=.5, reflection=.25):
		self.vertex = np.array(vertex)
		self.compute_normal()
		super().__init__(np.array(vertex[1]), np.array(color), diffuse_c, specular_c, reflection)

	def compute_normal(self):
		edge1 = self.vertex[1] - self.vertex[0]
		edge2 = self.vertex[2] - self.vertex[0]
		N = np.cross(edge1,edge2)
		#N /= N.sum()
		self.normal = normalize(N)

	def intersect(self, O, D):
		# Trumbore Algorithm
		edge1 = self.vertex[1] - self.vertex[0]
		edge2 = self.vertex[2] - self.vertex[0]
		eps = .00001
		pvec = np.cross(D, edge2)
		det = edge1.dot(pvec)
		if abs(det) < eps:
			return np.inf
		inv_det = 1. / det
		tvec = O - self.vertex[0]
		u = tvec.dot(pvec) * inv_det
		if u < 0. or u > 1.:
			return np.inf
		qvec = np.cross(tvec, edge1)
		v = D.dot(qvec) * inv_det
		if v < 0. or u + v > 1.:
			return np.inf
		t = edge2.dot(qvec) * inv_det
		if t < eps:
			return np.inf

		hit = np.array([t,u,v])
		dist = np.linalg.norm(O-hit)

		return float(dist)

	def get_normal(self, M):
		return self.normal

	def __str__(self):
		return f'Triangle (v1={self.vertex[0]}, v2={self.vertex[1]}, v3={self.vertex[2]})'
