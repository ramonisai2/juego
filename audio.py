import pygame
pygame.mixer.init()
def play_music(path):
pygame.mixer.music.load(path)
pygame.mixer.music.play(-1)
def play_sound(path):
sound = pygame.mixer.Sound(path)
sound.play()