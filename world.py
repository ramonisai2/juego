from OpenGL.GL import *
import random
import math

CHUNK_SIZE = 16
RENDER_DISTANCE = 3

class World:
    def __init__(self):
        self.chunks = {}
        self.generate_world()

    def generate_world(self):
        for x in range(-5, 5):
            for z in range(-5, 5):
                self.chunks[(x, z)] = self.generate_chunk(x, z)

    def generate_chunk(self, cx, cz):
        data = []
        for x in range(CHUNK_SIZE):
            for z in range(CHUNK_SIZE):
                world_x = cx * CHUNK_SIZE + x
                world_z = cz * CHUNK_SIZE + z
                height = math.sin(world_x * 0.2) * 2
                data.append((world_x, height, world_z))
        return data

    def render(self, player):
        player_chunk_x = math.floor(player.x / CHUNK_SIZE)
        player_chunk_z = math.floor(player.z / CHUNK_SIZE)
        glColor3f(0.2, 0.8, 0.2)
        for key, chunk in self.chunks.items():
            cx, cz = key
            dx = abs(cx - player_chunk_x)
            dz = abs(cz - player_chunk_z)
            if dx > RENDER_DISTANCE:
                continue
            if dz > RENDER_DISTANCE:
                continue
            for block in chunk:
                x, y, z = block
                glBegin(GL_QUADS)
                glVertex3f(x, y, z)
                glVertex3f(x + 1, y, z)
                glVertex3f(x + 1, y, z + 1)
                glVertex3f(x, y, z + 1)
                glEnd()
