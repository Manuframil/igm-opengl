# igm-opengl

## Ray-tracing

### Requisites
 - python3
 - numpy
 - matplotlib

### Files
 - raytracing.py -> Main file that creates the scene and figures
 - scene.py -> Scene class. Implements the ray-tracing algorithm to render. Requires a Camera, a number of Figures and a number of Lights.
 - camera.py -> Camera of the scene. Requires position and direction.
 - light.py -> A scene might have several lights. Each light has a position and a color.
 - figure.py -> Abstract class for the figures of the scene.
 - sphere.py & triangle.py & plane.py -> Concrete figures of the scene. Each one implements it's own methods to compute the intersection.
 - triangle_strip.py -> Class to create a strip of triangles given a list of vertex.
 - util.py -> Common functions.

### Usage

Configure the scene in the main file "raytracing.py" and execute it.
```
python3 raytracing.py
```
