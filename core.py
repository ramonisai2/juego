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

        # Viewport
        glViewport(0, 0, self.width, self.height)

        # Proyección
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        gluPerspective(
            70,
            self.width / self.height,
            0.1,
            100.0
        )

        glMatrixMode(GL_MODELVIEW)

        # Configuración OpenGL
        glEnable(GL_DEPTH_TEST)

        glClearColor(0.1, 0.1, 0.15, 1)

        self.clock = pygame.time.Clock()

        self.angle = 0

        self.running = True

    def update(self):

        self.angle += 1

    def draw_cube(self):

        glBegin(GL_QUADS)

        # Frente
        glColor3f(1, 0, 0)
        glVertex3f(-1, -1,  1)
        glVertex3f( 1, -1,  1)
        glVertex3f( 1,  1,  1)
        glVertex3f(-1,  1,  1)

        # Atrás
        glColor3f(0, 1, 0)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1,  1, -1)
        glVertex3f( 1,  1, -1)
        glVertex3f( 1, -1, -1)

        # Izquierda
        glColor3f(0, 0, 1)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1, -1,  1)
        glVertex3f(-1,  1,  1)
        glVertex3f(-1,  1, -1)

        # Derecha
        glColor3f(1, 1, 0)
        glVertex3f(1, -1, -1)
        glVertex3f(1,  1, -1)
        glVertex3f(1,  1,  1)
        glVertex3f(1, -1,  1)

        # Arriba
        glColor3f(1, 0, 1)
        glVertex3f(-1, 1, -1)
        glVertex3f(-1, 1,  1)
        glVertex3f( 1, 1,  1)
        glVertex3f( 1, 1, -1)

        # Abajo
        glColor3f(0, 1, 1)
        glVertex3f(-1, -1, -1)
        glVertex3f( 1, -1, -1)
        glVertex3f( 1, -1,  1)
        glVertex3f(-1, -1,  1)

        glEnd()

    def render(self):

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()

        glTranslatef(0, 0, -5)

        glRotatef(self.angle, 1, 1, 0)

        self.draw_cube()

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