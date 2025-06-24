import pygame


class Field():
    def __init__(self, screen, windows_size:tuple, size:int=10, count:int=100):
        '''
        
        '''
        
        self.screen = screen
        self.width = windows_size[0]
        self.height = windows_size[1]
        self.size = size
        self.count = count
        
        self.cellular_color = (128, 128, 128)
        
    def show(self):
        '''
        
        '''
        
        for x in range(0, self.width, self.size):
            for y in range(0, self.height, self.size):
                rect = pygame.Rect(x, y, self.size, self.size)
                pygame.draw.rect(self.screen, self.cellular_color, rect, 1)
