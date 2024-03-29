from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import numpy as np
from math import *


def axis():
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex(0,0,0)
    glVertex(10,0,0)

    glColor3f(0, 0, 0.4)
    glVertex(0, 0, 0)
    glVertex(0,10,0)

    glColor3f(0, 1, 0)
    glVertex(0, 0, 0)
    glVertex(0, 0, 10)

    glEnd()

def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60,1,0.1,50)
    gluLookAt(8,9,10,
              0,0,0,
              0,1,0)
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)


angle=0
x=0
forward = True

def display():
    global angle
    global x
    global forward

    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glClearColor(0.2,0.7,1,0)

    glLoadIdentity()     #Green_Land
    glBegin(GL_POLYGON)
    glColor3f(0, 0.7, 0.2)
    glVertex(9.5, 0, -6)
    glVertex(9.5, 0, -17)
    glVertex(-50, 0, -17)
    glVertex(-50, 0, -6)
    glEnd()

    glLoadIdentity()    #Green_Land
    glBegin(GL_POLYGON)
    glColor3f(0, 0.7, 0.2)
    glVertex(9.5, 0, 6)
    glVertex(9.5, 0, 100)
    glVertex(-40, 0, 100)
    glVertex(-40, 0, 6)
    glEnd()

    glLoadIdentity()
    glBegin(GL_POLYGON)     #main_road
    glColor3f(0,0,0.1)
    glVertex(9.5,0,-6)
    glVertex(9.5,0,6)
    glVertex(-40,0,6)
    glVertex(-40,0,-6)
    glEnd()

    glLoadIdentity()
    glBegin(GL_POLYGON)
    glColor3f(1,1,1)
    glVertex(6,0,-5.8)
    glVertex(6,0,-5.3)
    glVertex(1.5,0,-5.3)
    glVertex(1.5,0,-5.8)
    glEnd()

    glLoadIdentity()
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(6, 0, -4.8)
    glVertex(6, 0, -4.3)
    glVertex(1.5, 0, -4.3)
    glVertex(1.5, 0, -4.8)
    glEnd()

    glLoadIdentity()
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(6, 0, 5.8)
    glVertex(6, 0, 5.3)
    glVertex(1.5, 0, 5.3)
    glVertex(1.5, 0, 5.8)
    glEnd()

    glLoadIdentity()
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(6, 0, 4.8)
    glVertex(6, 0, 4.3)
    glVertex(1.5, 0, 4.3)
    glVertex(1.5, 0, 4.8)
    glEnd()

    glLoadIdentity()
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-6, 0, -5.8)
    glVertex(-6, 0, -5.3)
    glVertex(-1.5, 0, -5.3)
    glVertex(-1.5, 0, -5.8)
    glEnd()

    glLoadIdentity()
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-6, 0, -4.8)
    glVertex(-6, 0, -4.3)
    glVertex(-1.5, 0, -4.3)
    glVertex(-1.5, 0, -4.8)
    glEnd()

    glLoadIdentity()
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-13.5, 0, -5.8)
    glVertex(-13.5, 0, -5.3)
    glVertex(-9, 0, -5.3)
    glVertex(-9, 0, -5.8)
    glEnd()

    glLoadIdentity()
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-13.5, 0, -4.8)
    glVertex(-13.5, 0, -4.3)
    glVertex(-9, 0, -4.3)
    glVertex(-9, 0, -4.8)
    glEnd()

    glLoadIdentity()
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-21, 0, -5.8)
    glVertex(-21, 0, -5.3)
    glVertex(-16.5, 0, -5.3)
    glVertex(-16.5, 0, -5.8)
    glEnd()

    glLoadIdentity()
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-21, 0, -4.8)
    glVertex(-21.5, 0, -4.3)
    glVertex(-16.5, 0, -4.3)
    glVertex(-16.5, 0, -4.8)
    glEnd()

    glLoadIdentity()
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-28.5, 0, -5.8)
    glVertex(-28.5, 0, -5.3)
    glVertex(-24, 0, -5.3)
    glVertex(-24, 0, -5.8)
    glEnd()

    glLoadIdentity()
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-28.5, 0, -4.8)
    glVertex(-28.5, 0, -4.3)
    glVertex(-24, 0, -4.3)
    glVertex(-24, 0, -4.8)
    glEnd()

    glLoadIdentity()
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-6, 0, 5.8)
    glVertex(-6, 0, 5.3)
    glVertex(-1.5, 0, 5.3)
    glVertex(-1.5, 0, 5.8)
    glEnd()

    glLoadIdentity()
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-6, 0, 4.8)
    glVertex(-6, 0, 4.3)
    glVertex(-1.5, 0, 4.3)
    glVertex(-1.5, 0, 4.8)
    glEnd()

    glLoadIdentity()
    #axis()

    glColor3f(0.3, 0.4, 0.5)
    glLoadIdentity()
    glTranslate(2.5+x, -0.5 * 0.25,- 2.5 * 0.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.2, 0.5, 12, 8)

    glColor3f(0.3, 0.4, 0.5)
    glLoadIdentity()
    glTranslate(-2.5 + x, -0.5 * 0.25, -2.5 * 0.5)
    glutWireTorus(0.2, 0.5, 12, 8)


    glColor3f(0,0,0.4)
    glLoadIdentity()
    glTranslate(x, 0, 0)
    glScale(1, 0.25, 0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glTranslate(x, 0, 0)
    glColor3f(0.3, 0.3, 0.5)
    glScale(1, 0.25, 0.5)
    glutWireCube(5)


    glColor3f(0.3, 0.4, 0.5)
    glLoadIdentity()
    glTranslate(-2.5+x, -0.5 * 0.25, 2.5 * 0.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.2, 0.5, 12, 8)


    glColor3f(0.3,0.3,0.5)
    glLoadIdentity()
    glTranslate(x, 5 * 0.25, 0)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)


    glColor3f(0,0,0.4)
    glLoadIdentity()
    glTranslate(x, 5 * 0.25, 0)
    glScale(0.5, 0.25, 0.5)
    glutWireCube(5)

    glColor3f(0.9, 1, 0.1)
    glLoadIdentity()
    glTranslate(2.6+ x, 0.2 * 0.25, 1.2 * 0.5)
    glutSolidSphere(0.23, 12, 12)

    glColor3f(0.3, 0.4, 0.5)
    glLoadIdentity()
    glTranslate(2.5 + x, -0.5 * 0.25, 2.5 * 0.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.2, 0.5, 12, 8)

    glColor3f(0.9, 1, 0.1)
    glLoadIdentity()
    glTranslate(2.6 + x, 0.2 * 0.25, -1.2 * 0.5)
    glutSolidSphere(0.23, 12, 12)



    if forward:
        angle -= 0.1
        x +=0.0005
        if x > 5:
            forward = False
    else:
        x-=0.0005
        angle+=0.1
        if x < -5:
            forward = True



    glutSwapBuffers()


    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500,500)
glutCreateWindow(b"First OpenGL program")
glutDisplayFunc(display)
glutIdleFunc(display)
myInit()
glutMainLoop()