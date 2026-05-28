import pygame
pygame.font.init()
font = pygame.font.SysFont('Arial', 24)
def draw_ui(player):
surface = pygame.display.get_surface()
health = font.render(f'Vida: {int(player.health)}', True, (255,255,255))
9
stamina = font.render(f'Stamina: {int(player.stamina)}', True, (255,255,
255))
hunger = font.render(f'Hambre: {int(player.hunger)}', True, (255,255,255))
surface.blit(health, (20,20))
surface.blit(stamina, (20,50))
surface.blit(hunger, (20,80))