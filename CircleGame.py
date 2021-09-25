import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("CircleDrop")


class Ball:
    def __init__(self, pos):
        self.pos = pos
        self.radius = randint(10, 100)
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.speed = 0

    def draw_ball(self):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

    def fall_ball(self):
        pass


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball = Ball(pygame.mouse.get_pos())
            ball.draw_ball()

    pygame.display.update()
