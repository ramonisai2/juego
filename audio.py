import pygame
try:
    pygame.mixer.init()
except Exception as e:
    print(f'Audio no disponible: {e}')

def play_music(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1)

def play_sound(path):
    sound = pygame.mixer.Sound(path)
    sound.play()
