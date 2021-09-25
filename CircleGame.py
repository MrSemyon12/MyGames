import pygame

pygame.init()

screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("CircleDrop")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    pygame.display.update()