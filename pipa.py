from pygame import init, QUIT, quit
from pygame.display import set_mode
from pygame.event import get
from pygame.display import flip
from pygame.time import wait

from OpenGL.GLU import gluPerspective, gluLookAt, gluNewQuadric,\
     gluQuadricNormals, GLU_SMOOTH, gluQuadricTexture, gluCylinder
from OpenGL.GLUT import glutInit, glutSolidTorus, glutSolidCube,\
     glutSolidSphere
from OpenGL.GL import glClearColor, glClear, glMaterialfv,\
                      GL_FRONT, GL_AMBIENT, GL_DIFFUSE,\
                      GL_SPECULAR, glMateriali, GL_SHININESS,\
                      glPushMatrix, glTranslatef, glRotatef,\
                      glScalef, glPopMatrix, GL_TRUE

def pp(met):
    glPushMatrix()
    met()
    glPopMatrix()

def draw_gun():
    # Setting up materials, ambient, diffuse, specular and shininess properties are all
    # different properties of how a material will react in low/high/direct light for
    # example.
    k = 0
    ambient_coeffsGray = [k, k, k, 1]
    k = 1
    diffuse_coeffsGray = [k, k, k, k]
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
    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)						# // Create Smooth Normals
    gluQuadricTexture(quadric, GL_TRUE)
    
    r, h = 1, 3
    pp(lambda : (gluCylinder(quadric, r, r, h, 32, 16),\
                 glutSolidSphere(r, 20, 20),\
                 glTranslatef(0, 0, h),\
                 glutSolidSphere(r, 20, 20))) 

    '''radius
    The radius of the sphere.
    slices
    The number of subdivisions around the Z axis (similar to lines of longitude).
    stacks
    The number of subdivisions along the Z axis (similar to lines of latitude).

    quad	
    Specifies the quadrics object (created with gluNewQuadric ).
    base	
    Specifies the radius of the cylinder at z = 0.
    top	
    Specifies the radius of the cylinder at z = height .
    height	
    Specifies the height of the cylinder.
    slices	
    Specifies the number of subdivisions around the z axis.
    stacks	
    Specifies the number of subdivisions along the z axis.
    '''

# Initialization of PyGame modules
init()
# Initialization of Glut library
glutInit()
# Setting up the viewport, camera, backgroud and display mode
display = (1280, 720)
set_mode(display, 1073741826)
k = 0
glClearColor(k, k, k, k) 
an, al = display
fov, ar, zn, zf = 60, an / al, 0, 50
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
    glRotatef(1, 0, -1, 0) # gira en sentido horario?

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
