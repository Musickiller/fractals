
import pyglet
import numpy as np
import math
sqrt = math.sqrt

window_width = 900
window_height = 780
window_caption = "Triangle Fractal"

fps = 30
xfps = 1/fps
dots_per_frame=20

x = 0
y = 0

window = pyglet.window.Window(
    window_width,
    window_height,
    caption=window_caption
    )


pixels = []

def generate_equal_triangle(l):
    '''
          A         AB=BC=AC=l
          .         C(0;0), B(CB, 0),
       .  |  .      AH = sqrt(AC^2+CH^2) =
    C ____|____ B   = sqrt(l^2 - (l/2)^2) =  h
          H	        A (l/2,AH)
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

    
def update(dt):
    global pixels
    global x
    global y
    global fig
    global pix_count
    global dots_per_frame
    nvrtx = len(fig)
    for i in range(dots_per_frame):
        vertex = int(np.random.rand()*nvrtx)
        pixels += [x, y]
        pix_count += 1
        x = (x+fig[vertex][0])/2
        y = (y+fig[vertex][1])/2
        #let's keep aligned to real pixles, please...
        x,y = int(x),int(y)
    
    
def init():
    pixels = []
    print ("Init figure")
    fig = generate_equal_triangle(window_width)
    pixels += pixels_from_figure(fig)
    print ("done")
    return fig, pixels
    

@window.event
def on_draw():
    global pixels
    npix=int(len(pixels)/2)
    # clear the window... well.. not really useful here, I think.
    window.clear()
    # draw existing points
    pyglet.graphics.draw(npix, pyglet.gl.GL_POINTS, ('v2i', pixels) )
    # mark current point:
    pyglet.graphics.draw(9, pyglet.gl.GL_POINTS,
        ('v2i', (
            x,y,
            x,y+1,
            x,y+2,
            x+1,y,
            x+2,y,
            x,y-1,
            x,y-2,
            x-1,y,
            x-2,y
        )),
        ('c3B', (255,255,0)*9)
    )
    # draw pixel count:
    label = pyglet.text.Label(str(pix_count),
                          font_name='Times New Roman',
                          font_size=10,
                          x=20, y=window.height-25)
    label.draw()

# anchor_x='center', anchor_y='center'

    
pix_count = 0
fig, pixels = init()

pyglet.clock.schedule_interval(update, xfps)

pyglet.app.run()

# while True:
    # pyglet.clock.tick()

    # for window in pyglet.app.windows:
        # window.switch_to()
        # window.dispatch_events()
        # window.dispatch_event('on_draw')
        # window.flip()
