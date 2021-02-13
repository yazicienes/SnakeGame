import pygame
import sys
import random


##constants
FPS = 10
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH/GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT/GRID_SIZE

UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake(object):
    def __init__(self):
        pass
    def get_head_position(self):
        pass
    def turn(self, point):
        pass
    def move(self):
        pass
    def reset(self):
        pass
    def handle_keys(self, surface):
        pass
    def draw(self, surface):
        pass

class Food(object):
    def __init__(self):
        pass
    def randomize_position(self):
        pass
    def draw(self, surface):
        pass


def drawGrid(surface):
    #game grid
    

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)
    snake = Snake()
    food = Food()
    score = 0
    #game loop
    while (True):
        clock.tick(FPS)
        screen.blit(surface, (0,0))
        pygame.display.update()

main()