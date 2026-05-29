import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Game:

    def __init__(self):

        pygame.init()

        self.width = 1280
        self.height = 720

        pygame.display.set_mode(
            (self.width, self.height),
            DOUBLEBUF | OPENGL
        )

        gluPerspective(70, self.width/self.height, 0.1, 500.0)
        glMatrixMode(GL_MODELVIEW)
        glClearColor(0.0, 0.0, 0.0, 1.0)

        glEnable(GL_DEPTH_TEST)

        self.clock = pygame.time.Clock()

        self.running = True

    def update(self):
        pass

    def render(self):

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()

        glTranslatef(0.0, 0.0, -5)

        glBegin(GL_QUADS)

        # Frente
        glColor3f(1, 0, 0)

        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)

        # Atrás
        glColor3f(0, 1, 0)

        glVertex3f(-1, -1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, -1, -1)

        glEnd()

        pygame.display.flip()

    def run(self):

        while self.running:

            self.clock.tick(60)

            for event in pygame.event.get():

                if event.type == QUIT:
                    self.running = False

            self.update()
            self.render()

        pygame.quit()