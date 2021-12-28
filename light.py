import numpy as np

class Light():
	def __init__(self, position, color):
		self.position = np.array(position)
		self.color = np.array(color)