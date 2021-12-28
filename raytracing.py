import numpy as np
import matplotlib.pyplot as plt
from sphere import Sphere
from plane import Plane
from triangle import Triangle
from light import Light
from camera import Camera
from scene import Scene


w = 400
h = 300

# List of objects.
color_plane0 = 1. * np.ones(3)
color_plane1 = 0. * np.ones(3)

scene = Scene(h,w)
scene.add_camera(Camera([0., 0.35, -1.], [0., 0., 0.]))
scene.add_lights( [
    Light([5., 5., -10.], [1., 0., 0.]), 
    Light([-5., 10., 20.], np.ones(3))
    ])
scene.add_figures([
    Sphere([.75, .1, 1.], .6, [1., 1., 1.]),
    Triangle([.5, .25, 1.], [1., 0., 0.], [[-.25, 0, 0], [0, .5, 0], [.25, 0, 0]], [0., 1., 0.], reflection = 0.),
    Plane([0., -.5, 0.], [0., 1., 0.], lambda M: (color_plane0 if (int(M[0] * 2) % 2) == (int(M[2] * 2) % 2) else color_plane1))
    ])

scene.draw()
scene.save()
