from OpenGL.GL import glViewport, glMatrixMode, GL_PROJECTION,\
     glLoadIdentity, glOrtho, GL_MODELVIEW, glClearColor,\
     glClear, glShadeModel, GL_SMOOTH, glTranslatef, glBegin,\
     GL_TRIANGLES, glColor3f, glVertex2f, glEnd, glFlush
from OpenGL.GLUT import glutInit, glutInitWindowSize,\
     glutCreateWindow, glutDisplayFunc, glutReshapeFunc,\
     glutMainLoop
 
def paint():
    k = 0.3
    glClearColor(k, k, k, 0)
    glClear(16640)
 
    glShadeModel(GL_SMOOTH)
    
    glLoadIdentity()
    glTranslatef(-15, -15, 0)
 
    glBegin(GL_TRIANGLES)
    
    glColor3f(1, 0, 0)
    glVertex2f(0, 0)
    glColor3f(0, 1, 0)
    glVertex2f(30, 0)
    glColor3f(0, 0, 1)
    glVertex2f(0, 30)
    glEnd()
 
    glFlush()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    a = 30
    b = -a    
    glOrtho(b, a, b, a, b, a)
    glMatrixMode(GL_MODELVIEW)
 
glutInit(1, 1)
glutInitWindowSize(640, 480)
glutCreateWindow("Triangle")

glutDisplayFunc(paint)
glutReshapeFunc(reshape)

glutMainLoop()
