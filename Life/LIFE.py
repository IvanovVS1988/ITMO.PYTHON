import pygame
import LifeLogic


print("Input width of screen")
width = int(input())
print("Input height of screen")
height = int(input())
print("Input CELL size")
cell = int(input())
print("FPS")
FPS = float(input())

W = int(width / cell)
H = int(height / cell)
RES = cell * W, cell * H
pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

current_field = LifeLogic.start_field(W, H)
nextstep_field = LifeLogic.start_field_next_step(W, H)

while True:
    surface.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    [pygame.draw.line(surface, pygame.Color('dimgray'), (x, 0), (x, cell * H)) for x in range(0, width, cell)]
    [pygame.draw.line(surface, pygame.Color('dimgray'), (0, y), (cell * W, y)) for y in range(0, height, cell)]

    for x in range(1, W - 1):
        for y in range(1, H - 1):
            if current_field[x][y] > 0:
                color = 255 - 3 * current_field[x][y]
                if color < 30:
                    color = 30
                pygame.draw.rect(surface, (0, color, 0), (x * cell , y * cell, cell, cell))
    nextstep_field = LifeLogic.field_next_step(W, H, current_field)
    current_field = nextstep_field

    pygame.display.flip()
    clock.tick(FPS)
