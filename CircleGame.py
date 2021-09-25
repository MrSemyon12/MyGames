import pygame
from random import randint

window_size = (1600, 900)
pygame.init()
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("CircleDrop")

ball_list = list()


class Ball:
    def __init__(self, pos):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.radius = randint(10, 100)
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.speed = 0

    def draw_ball(self):
        pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.radius)

    def fall_ball(self):
        if self.pos_y < window_size[1]:
            self.pos_y += 1
        else:
            self.pos_y = window_size[1]


def draw_balls():
    for element in ball_list:
        element.draw_ball()


def fall_balls():
    for element in ball_list:
        element.fall_ball()


while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball = Ball(pygame.mouse.get_pos())
            ball_list.append(ball)

    draw_balls()
    fall_balls()

    pygame.display.update()
