#Ejemplo Vertex buffer object VRAM
from pygame import init, OPENGL, DOUBLEBUF, QUIT, quit
from pygame.display import set_mode, flip
from pygame.event import get
from OpenGL.GL import *
from ctypes import c_float

init()
screen = set_mode((800, 600), OPENGL|DOUBLEBUF, 24)
glViewport(0, 0, 800, 600)
glClearColor(0, 0.5, 0.5, 1)
glEnableClientState(GL_VERTEX_ARRAY)

vertices = (0, 1, 0,  0, 0, 0,  1, 1, 0)
vbo = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vbo)
glBufferData(GL_ARRAY_BUFFER, 4 * len(vertices),\
            (c_float * len(vertices))(*vertices),\
            GL_STATIC_DRAW)

running = True
while running:
    glClear(GL_COLOR_BUFFER_BIT)

    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glVertexPointer(3, GL_FLOAT, 0, None)

    glDrawArrays(GL_TRIANGLES, 0, 3)

    flip()

    for event in get():
        if event.type == QUIT:
            running = False
            quit()
