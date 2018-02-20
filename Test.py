from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
def plotfunc():
    glClearColor(0, 0.61, 0.98, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    #HEAD

    glBegin(GL_POLYGON)
    glColor(0.8,0.2,0)
    r = .3
    for theta in np.arange(0, 2 * pi, 0.1):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex2d(x, y + 0.45)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(1, .8 , .41)
    r=0.05
    for theta in np.arange(0, 2*pi, 0.1):
        x=r*cos(theta)
        y=r*sin(theta)
        glVertex2d(x+.12, y+0.35)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(1, .8 , .41)
    r = 0.05
    for theta in np.arange(0, 2 * pi, 0.1):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex2d(x-.12, y + 0.35)
    glEnd()


    glBegin(GL_POLYGON)
    glColor(1, .8 , .41)
    r = .1
    for theta in np.arange(0, 2 * pi, 0.1):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex2d(x, y + 0.35)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(1, 1, 1)
    r = .08
    for theta in np.arange(0, 2 * pi, 0.1):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex2d(x-.20, y + 0.48)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(1, 1, 1)
    r = .08
    for theta in np.arange(0, 2 * pi, 0.1):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex2d(x+.20, y + 0.48)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0, 0, 0)
    r = .06
    for theta in np.arange(0, 2 * pi, 0.1):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex2d(x + .22, y + 0.48)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0, 0, 0)
    r = .06
    for theta in np.arange(0, 2 * pi, 0.1):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex2d(x -.22, y + 0.48)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(0, 0, 0)
    r = .02
    for theta in np.arange(0, 2 * pi, 0.1):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex2d(x -.05 , y + 0.40)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(.8, .2, 0)
    r = .4
    for theta in np.arange(0, 2 * pi, 0.1):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex2d(x , y -.20)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(.8, .2, 0)
    r = .35
    for theta in np.arange(0, 2 * pi, 0.1):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex2d(x-.20, y - .25)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(.8, .2, 0)
    r = .35
    for theta in np.arange(0, 2 * pi, 0.1):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex2d(x + .20, y - .25)
    glEnd()

    




    glFlush()
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Ugandan_Knuckles")
glutDisplayFunc(plotfunc)
glutMainLoop()