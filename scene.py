import numpy as np
import matplotlib.pyplot as plt
from util import normalize


class Scene():
	def __init__(self, height, width):
		self.height = height
		self.width = width
		self.img = np.zeros((height, width, 3))
		self._ambient = .05
		self._diffuse_c = 1.
		self._specular_c = 1.
		self._specular_k = 50
		self._camera = None
		self._lights = []
		self._figures = []
		self.depth_max = 5

	def add_camera(self, camera):
		self._camera = camera

	def add_light(self, light):
		self._lights.append(light)

	def add_lights(self, lights):
		self._lights = lights

	def add_figure(self, figure):
		self._figures.append(figure)

	def add_figures(self, figures):
		self._figures = figures

	def save(self, filename = 'fig.png'):
		plt.imsave(filename, self.img)

	def trace_ray(self, rayO, rayD):
		# Find first point of intersection with the scene.
		t = np.inf
		for i, obj in enumerate(self._figures):
			t_obj = obj.intersect(rayO, rayD)
			if t_obj < t:
				t, obj_idx = t_obj, i
		# Return None if the ray does not intersect any object.
		if t == np.inf:
			return 
		# Find the object.
		obj = self._figures[obj_idx]
		# Find the point of intersection on the object.
		M = rayO + rayD * t
		# Find properties of the object.
		N = obj.get_normal(M)
		color = obj.get_color(M)
		# Start computing the color.
		col_ray = self._ambient
		for light in self._lights:
			toL = normalize(light.position - M)
			toO = normalize(self._camera.position - M)
			# Shadow: find if the point is shadowed or not.
			l = [obj_sh.intersect(M + N * .0001, toL) for k, obj_sh in enumerate(self._figures) if k != obj_idx]
			if l and np.min(l) < np.inf:
				continue
			# Lambert shading (diffuse).
			col_ray += obj.diffuse_c * max(np.dot(N, toL), 0) * color
			# Blinn-Phong shading (specular).
			col_ray += obj.specular_c * max(np.dot(N, normalize(toL + toO)), 0) ** self._specular_k * light.color
		return obj, M, N, col_ray

	def draw(self):
		r = float(self.width) / self.height
		S = (-1., -1. / r + .25, 1., 1. / r + .25)
		col = np.zeros(3)

		for i, x in enumerate(np.linspace(S[0], S[2], self.width)):
			if i % 10 == 0:
				print(f'{i / float(self.width) * 100}%')
			for j, y in enumerate(np.linspace(S[1], S[3], self.height)):
				col[:] = 0
				self._camera.direction[:2] = (x, y)
				D = normalize(self._camera.direction - self._camera.position)
				depth = 0
				rayO, rayD = self._camera.position, D
				reflection = 1.
				# Loop through initial and secondary rays.
				while depth < self.depth_max:
				    traced = self.trace_ray(rayO, rayD)
				    if not traced:
				        break
				    obj, M, N, col_ray = traced
				    # Reflection: create a new ray.
				    rayO, rayD = M + N * .0001, normalize(rayD - 2 * np.dot(rayD, N) * N)
				    depth += 1
				    col += reflection * col_ray
				    reflection *= obj.reflection
				self.img[self.height - j - 1, i, :] = np.clip(col, 0, 1)