import numpy as np
from figure import Figure

class Triangle(Figure):
	def __init__(self, position, normal, vertex, color, diffuse_c=.75, specular_c=.5, reflection=.25):
		self.normal = np.array(normal)
		self.vertex = np.array(vertex)
		super().__init__(np.array(position), np.array(color), diffuse_c, specular_c, reflection)

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
