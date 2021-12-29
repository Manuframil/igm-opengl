import numpy as np
import matplotlib.pyplot as plt
from sphere import Sphere
from plane import Plane
from triangle import Triangle
from light import Light
from camera import Camera
from scene import Scene
from triangle_strip import TriangleStrip

w = 400
h = 300

# List of objects.
color_plane0 = 1. * np.ones(3)
color_plane1 = 0. * np.ones(3)

scene = Scene(h,w, name='Amazing scene')
scene.add_camera(Camera([0., 0.35, -1.], [0., 0., 0.]))
scene.add_lights( [
    Light([5., 5., -10.], [1., 0., 0.]), 
    Light([-5., 10., 20.], np.ones(3))
    ])

ml = np.array([-.5, 0, 0])
v = [[-.25, .75, 0]+ml, [.25, .75, 0,]+ml, [0.25, 0.25, .0]+ml, [.75, .5, 0]+ml]
#v = [[-.5, .5, 0], [0, .5, 0,], [0., 0, .5], [.5, .5, 0], [.5, 0, 0], [0., 0, 0.5], [.5, -.5, 0], [0, -.5, 0], [0, 0, 0.5], [-.5, -.5, 0], [-.5, 0, 0], [0, 0, 0.5], [-.5, .5, 0]]

scene.add_figures(TriangleStrip(vertex = v, color = [1, 0.0, 0.5], reflection = 0.0, diffuse_c=.0, specular_c=.0).get_strip())
scene.add_figures([
    Sphere( position = [.75, .1, 1.], radius = .6, color = [0., 0., 1.]),
    Triangle(vertex = [[-.25, 0, 0], [-.25, 0.25, 0], [0, 0, 0.4]],color = [0., 1.0, 0.98], reflection = 0.0),
    Plane([0., -.5, 0.], [0., 1., 0.], lambda M: (color_plane0 if (int(M[0] * 2) % 2) == (int(M[2] * 2) % 2) else color_plane1))
    ])

print(scene)
scene.draw(verbose=1)
scene.save()
