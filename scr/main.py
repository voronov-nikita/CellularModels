from Piece import *
import pygame


class MainWindow():
    def __init__(self, width:int, height:int, titleWindow:str) -> None:
        '''

        '''
        self.width = width
        self.height = height
        
        self.screen = pygame.display.set_mode((width, height-1))
        pygame.display.set_caption(titleWindow)
        
    def initBoard(self) -> None:
        '''
        
        '''
        num = self.width // 8 + 1
        for row in range(num):
            for col in range(num):
                color = ("#242424", "white")[(row+col)%2==0]
                pygame.draw.rect(self.screen, color, (col*num, row*num, num, num))
                
    def initModels(self):
        '''
        
        '''
        pass


def main():
    '''
    
    '''
    pygame.init()
    window = MainWindow(500, 500, "PyChess")
    window.initBoard()
    while pygame.QUIT not in [event.type for event in pygame.event.get()]:
        pygame.display.flip()


if __name__=="__main__":
    main()