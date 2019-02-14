import pyglet
import numpy as np
import math
sqrt = math.sqrt

window_width = 900
window_height = 780
window_caption = "Triangle Fractal"


window = pyglet.window.Window(
	window_width,
	window_height,
	caption=window_caption
	)

def generate_equal_triangle(l):
	'''
  		  A			  AB=BC=AC=l
  		  .			  C(0;0), B(CB, 0),
	   .  |  .		AH = sqrt(AC^2+CH^2) =
	C ____|____ B	  = sqrt(l^2 - (l/2)^2) =  h
	      H			  A (l/2,AH)
	'''
	C = [0,0]
	B = [l,0]
	h = sqrt (l**2 - (l/2)**2)
	A = [int(l/2), int(h)]
	return [A,B,C]

def pixels_from_figure(fig):
	pixs = []
	for dot in fig:
		pixs += dot
	return pixs

def make_fractal(fig, start=[0,0], ndots=1000000):
	x = start[0]
	y = start[1]
	nvrtx = len(fig)
	pixels = []
	for i in range(ndots):
		vertex = int(np.random.rand()*nvrtx)
		x = (x+fig[vertex][0])/2
		y = (y+fig[vertex][1])/2
		pixels += [int(x), int(y)]
	return pixels

@window.event
def on_draw():
	pixels = []
	print ("Init figure")
	fig = generate_equal_triangle(window_width)
	pixels += pixels_from_figure(fig)
	print ("done")
	print ("Make fractal")
	pixels += make_fractal(fig)
	print ("done")
	
	npix=int(len(pixels)/2)
	window.clear()
	pyglet.graphics.draw(npix, pyglet.gl.GL_POINTS,
		('v2i', pixels)
	)
    
pyglet.app.run()

