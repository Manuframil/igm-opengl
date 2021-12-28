import numpy as np

class Camera():
	def __init__(self, position, direction):
		self.position = np.array(position)
		self.direction = np.array(direction)