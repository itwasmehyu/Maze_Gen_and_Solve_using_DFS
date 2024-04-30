import pygame
from random import choice
import time

clock = pygame.time.Clock()
WIDTH = 1200
HEIGHT = 600

class Cell:
    def __init__(self, x, y,tile):
        self.x, self.y = x, y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False
        self.thickness = 4
        self.TILE = tile

    def draw(self,sc):
        x, y = self.x * self.TILE, self.y * self.TILE

        if self.walls['top']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x, y), (x + self.TILE, y), self.thickness)
        if self.walls['right']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x + self.TILE, y), (x + self.TILE, y + self.TILE), self.thickness)
        if self.walls['bottom']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x + self.TILE, y + self.TILE), (x , y + self.TILE), self.thickness)
        if self.walls['left']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x, y + self.TILE), (x, y), self.thickness)
            
    def draw_inside(self,sc,color):
        x, y = self.x * self.TILE, self.y * self.TILE
        inner_square_size = self.TILE // 2  
        inner_square_top_left_x = x + inner_square_size // 2  
        inner_square_top_left_y = y + inner_square_size // 2  

        pygame.draw.rect(sc, color, (inner_square_top_left_x, inner_square_top_left_y, inner_square_size, inner_square_size))
    def get_rects(self):
        rects = []
        x, y = self.x * self.TILE, self.y * self.TILE
        if self.walls['top']:
            rects.append(pygame.Rect( (x, y), (self.TILE, self.thickness) ))
        if self.walls['right']:
            rects.append(pygame.Rect( (x + self.TILE, y), (self.thickness, self.TILE) ))
        if self.walls['bottom']:
            rects.append(pygame.Rect( (x, y + self.TILE), (self.TILE , self.thickness) ))
        if self.walls['left']:
            rects.append(pygame.Rect( (x, y), (self.thickness, self.TILE) ))
        return rects

    def check_cell(self, x, y):
        cols = WIDTH // self.TILE
        rows = HEIGHT // self.TILE
        find_index = lambda x, y: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return self.grid_cells[find_index(x, y)]

    def check_neighbors(self, grid_cells):
        self.grid_cells = grid_cells
        neighbors = []
        top = self.check_cell(self.x, self.y - 1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return choice(neighbors) if neighbors else False
