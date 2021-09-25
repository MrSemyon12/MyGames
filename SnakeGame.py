import pygame
from random import randint

pygame.init()

screen_size = 800
block_size = 40
update_snake = 0
blocks_amount = int(screen_size / block_size)

screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("SnakeGame")


def rand_pos():
    return [randint(0, blocks_amount - 1), randint(0, blocks_amount - 1)]


class Manager:
    def __init__(self):
        self.is_running = True
        self.current_food = Food()
        self.current_snake = Snake()
        self.score = 0
        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.text_surface = self.my_font.render(f'Score: {self.score}', True, (255, 0, 0))

    def check_collision(self):
        if self.current_food.pos in self.current_snake.pos:
            self.current_snake.need_grow = True
            self.current_food.pos = rand_pos()
            self.score += 1
            self.text_surface = self.my_font.render(f'Score: {self.score}', True, (255, 0, 0))
            while self.current_food.pos in self.current_snake.pos:
                self.current_food.pos = rand_pos()

        if self.current_snake.is_bumped():
            self.my_font = pygame.font.SysFont('Comic Sans MS', 60)
            self.text_surface = self.my_font.render(f'WASTED! score: {self.score}', True, (255, 0, 0))
            self.is_running = False


class Background:
    def __init__(self):
        self.green1 = (146, 239, 162)
        self.green2 = (128, 208, 119)

    def draw(self):
        for rows in range(blocks_amount):
            for columns in range(blocks_amount):
                if (columns + rows) % 2 == 0:
                    color = self.green1
                else:
                    color = self.green2
                pygame.draw.rect(screen, color, [columns * block_size, rows * block_size, block_size, block_size])


class Food:
    def __init__(self):
        self.pos = [int(blocks_amount / 2) - 1, int(blocks_amount / 2) - 1]
        self.RED = (195, 40, 40)

    def draw(self):
        pygame.draw.rect(screen, self.RED, [self.pos[0] * block_size,
                                            self.pos[1] * block_size,
                                            block_size, block_size])


class Snake:
    def __init__(self):
        self.color = (30, 100, 20)
        self.pos = [[int(blocks_amount / 2), int(blocks_amount / 2)],
                    [int(blocks_amount / 2), int(blocks_amount / 2) + 1],
                    [int(blocks_amount / 2), int(blocks_amount / 2) + 2],
                    [int(blocks_amount / 2), int(blocks_amount / 2) + 3]]
        self.direct = [0, -1]
        self.size = 4
        self.need_grow = False

    def draw(self):
        for current in self.pos:
            pygame.draw.rect(screen, self.color, [current[0] * block_size,
                                                  current[1] * block_size,
                                                  block_size, block_size])

    def move(self):
        new_pos = list()
        new_pos.append([self.pos[0][0] + self.direct[0], self.pos[0][1] + self.direct[1]])

        if not self.need_grow:
            for current in self.pos[:-1]:
                new_pos.append(current)
        else:
            self.need_grow = False
            for current in self.pos:
                new_pos.append(current)

        for current in new_pos:
            if current[0] == blocks_amount:
                current[0] = 0
            if current[1] == blocks_amount:
                current[1] = 0
            if current[0] == -1:
                current[0] = blocks_amount - 1
            if current[1] == -1:
                current[1] = blocks_amount - 1
        self.pos = new_pos

    def is_bumped(self):
        for current in self.pos:
            flag = 0
            for i in self.pos:
                if i == current:
                    flag += 1
            if flag > 1:
                return True
        return False


def check_win(mng: Manager):
    if mng.score == blocks_amount * blocks_amount - 4:
        mng.is_running = False
        manager.text_surface = manager.my_font.render(f'WINNER! score: {manager.score}', True, (255, 0, 0))


manager = Manager()
bg = Background()

# main loop
while True:
    bg.draw()
    screen.blit(manager.text_surface, (0, 0))
    check_win(manager)

    if manager.is_running:
        manager.current_food.draw()
        manager.current_snake.draw()
        if update_snake > 99:
            update_snake = 0
            manager.current_snake.move()

    else:
        manager.current_snake.draw()
    manager.check_collision()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and manager.current_snake.direct != [0, 1]:
                manager.current_snake.direct = [0, -1]
            elif event.key == pygame.K_a and manager.current_snake.direct != [1, 0]:
                manager.current_snake.direct = [-1, 0]
            elif event.key == pygame.K_s and manager.current_snake.direct != [0, -1]:
                manager.current_snake.direct = [0, 1]
            elif event.key == pygame.K_d and manager.current_snake.direct != [-1, 0]:
                manager.current_snake.direct = [1, 0]

    pygame.display.update()
    update_snake += 0.6