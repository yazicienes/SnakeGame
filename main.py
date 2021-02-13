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

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))] 
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (0, 0, 0)
        
    def get_head_position(self):
        return self.positions[0]

    def turn(self, dir):
        self.direction = dir

    def move(self):
        cur_pos = self.get_head_position()
        x,y = self.direction
        new_pos = (((cur_pos[0] + (x*GRID_SIZE)) % SCREEN_WIDTH), (cur_pos[1] + (y*GRID_SIZE)) % SCREEN_HEIGHT)
        self.positions.insert(0, new_pos)
        if (len(self.positions) > self.length):
            self.positions.pop()

    def reset(self):
        pass
    def handle_keys(self, surface):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (90,123,200), r, 1)


class Food(object):
    def __init__(self):
        pass
    def randomize_position(self):
        pass
    def draw(self, surface):
        pass


def drawGrid(surface):
    #game grid
    for y in range(0, SCREEN_HEIGHT):
        for x in range(0, SCREEN_WIDTH):
            if (x+y) % 2 == 0: #every other 1 unit
                r = pygame.Rect((x*GRID_SIZE, y*GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, (153, 230, 153), r)
            else: #every other 1 unit
                r2 = pygame.Rect((x*GRID_SIZE, y*GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, (153, 230, 153), r2)


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    snake = Snake()
    food = Food()
    score = 0
    #game loop
    while (True):
        clock.tick(FPS)

        snake.handle_keys(surface)
        drawGrid(surface)
        snake.move()
        snake.draw(surface)

        screen.blit(surface, (0,0))
        pygame.display.update()

main()