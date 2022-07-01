from pygame import init, QUIT, quit
from pygame.display import set_mode
from pygame.event import get
from pygame.display import flip
from pygame.time import wait

from OpenGL.GL import glClearColor, glClear, glMaterialfv,\
     GL_FRONT, GL_AMBIENT, GL_DIFFUSE, GL_SPECULAR, glMateriali,\
     GL_SHININESS, glPushMatrix, glTranslatef, glRotatef,\
     glScalef, glPopMatrix
from OpenGL.GLU import gluPerspective, gluLookAt
from OpenGL.GLUT import glutInit, glutSolidTorus, glutSolidCube

def pp(ms):
    glPushMatrix()

    for m in ms:
        m()

    glPopMatrix()

def draw_gun():
    # Setting up materials, ambient, diffuse, specular and shininess properties are all
    # different properties of how a material will react in low/high/direct light for
    # example.
    k = 0.3
    ambient_coeffsGray = [k, k, k, 1]
    k = 0.5
    diffuse_coeffsGray = [k, k, k, 1]
    k = 0
    specular_coeffsGray = [k, k, k, 1]

    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient_coeffsGray)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse_coeffsGray)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular_coeffsGray)
    glMateriali(GL_FRONT, GL_SHININESS, 1)

    # OpenGL is very finicky when it comes to transformations, for all of them are global,
    # so it's good to seperate the transformations which are used to generate the object
    # from the actual global transformations like animation, movement and such.
    # The glPushMatrix() ----code----- glPopMatrix() just means that the code in between
    # these two functions calls is isolated from the rest of your project.
    # Even inside this push-pop (pp for short) block, we can use nested pp blocks,
    # which are used to further isolate code in it's entirety.
    pp((lambda : pp((lambda : glTranslatef(3.1, 0, 1.75),\
                     lambda : glRotatef(90, 0, 1, 0),\
                     lambda : glScalef(1, 1, 5),\
                     lambda : glScalef(0.2, 0.2, 0.2),\
                     lambda : glutSolidTorus(0.2, 1, 10, 10))),\

        lambda : pp((lambda : glTranslatef(2.5, 0, 1.75),\
                     lambda : glScalef(0.1, 0.1, 1),\
                     lambda : glutSolidCube(1))),\

        lambda : pp((lambda : glTranslatef(1, 0, 1),\
                     lambda : glRotatef(10, 0, 1, 0),\
                     lambda : glScalef(0.1, 0.1, 1),\
                     lambda : glutSolidCube(1))),\

        lambda : pp((lambda : glTranslatef(0.8, 0, 0.8),\
                     lambda : glRotatef(90, 1, 0, 0),\
                     lambda : glScalef(0.5, 0.5, 0.5),\
                     lambda : glutSolidTorus(0.2, 1, 10, 10))),\

        lambda : pp((lambda : glTranslatef(1, 0, 1.5),\
                     lambda : glRotatef(90, 0, 1, 0),\
                     lambda : glScalef(1, 1, 4),\
                     lambda : glutSolidCube(1))),\

        lambda : pp((lambda : glRotatef(8, 0, 1, 0),\
                     lambda : glScalef(1.1, 0.8, 3),\
                     lambda : glutSolidCube(1)))))

# Initialization of PyGame modules
init()
# Initialization of Glut library
glutInit()
# Setting up the viewport, camera, backgroud and display mode
display = (1280, 720)
set_mode(display, 1073741826)
k = 0.1
glClearColor(k, k, k, 3 * k) 
an, al = display
fov, ar, zn, zf = 60, an / al, 0.1, 50
gluPerspective(fov, ar, zn, zf)
x, y, z = (5, 5, 0)
c_X, c_Y, c_Z = (0, 0, 0)
u_X, u_Y, u_Z = (0, 0, 1) #rot
gluLookAt(x, y, z, c_X, c_Y, c_Z, u_X, u_Y, u_Z)

esta_Func = True

while esta_Func:
    # Clears the screen for the next frame to be drawn over
    glClear(16640)
    ############## INSERT CODE FOR GENERATING OBJECTS ##################
    draw_gun()
    ####################################################################
    # Function used to advance to the next frame essentially
    flip()
    wait(10) #ms 90fps

    # Listener for exit command
    for event in get():
        if event.type == QUIT:
            esta_Func = False
            quit()
