from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
class Player:
def __init__(self):
self.x = 0
3
self.y = 2
self.z = 0
self.rot_y = 0
self.speed = 0.15
self.health = 100
self.hunger = 100
self.stamina = 100
self.inventory = []
def update(self, keys):
if keys[pygame.K_w]:
self.z-= self.speed
if keys[pygame.K_s]:
self.z += self.speed
if keys[pygame.K_a]:
self.x-= self.speed
if keys[pygame.K_d]:
self.x += self.speed
if keys[pygame.K_LSHIFT]:
self.speed = 0.25
self.stamina-= 0.2
else:
self.speed = 0.15
if self.stamina < 0:
self.stamina = 0
def apply_camera(self):
glRotatef(self.rot_y, 0,1,0)
glTranslatef(-self.x,-self.y,-self.z)