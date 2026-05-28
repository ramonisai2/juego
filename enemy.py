from OpenGL.GL import *
import math
class Enemy:
def __init__(self, x,y,z):
self.x = x
self.y = y
self.z = z
self.health = 100
self.speed = 0.03
def update(self, player):
dx = player.x- self.x
dz = player.z- self.z
dist = math.sqrt(dx*dx + dz*dz)
if dist < 20:
if dist > 1:
self.x += dx * self.speed
self.z += dz * self.speed
else:
player.health-= 0.05
def render(self):
glPushMatrix()
glTranslatef(self.x, self.y, self.z)
glColor3f(1,0,0)
size = 1
glBegin(GL_QUADS)
glVertex3f(-size,0,-size)
5
glVertex3f(size,0,-size)
glVertex3f(size,2,-size)
glVertex3f(-size,2,-size)
glEnd()
glPopMatrix()