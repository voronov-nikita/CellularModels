# 
# The part where the main classes for working with chess pieces are presented. 
# The submitted classes are imported directly into the project file. 
# 
# All classes of shapes are presented in one variant for each of the 
# possible colors of the shape
# 


import pygame
import math


class Pawn():
    def __init__(self, color:str) -> None:
        self.image:str = ("../assets/black_pawn.png", "../assets/white_pawn.png")[color=="black"]
        


class Queen():
    def __init__(self, color:str) -> None:
        self.image:str = ("../assets/black_queen.png", "../assets/white_queen.png")[color=="black"]



class Rook():
    def __init__(self, color) -> None:
        self.image:str = ("../assets/black_rook.png", "../assets/white_rook.png")[color=="black"]



class Knight():
    def __init__(self, color:str) -> None:
        self.image:str = ("../assets/black_knight.png", "../assets/white_knight.png")[color=="black"]


class Bishop():
    def __init__(self, color:str) -> None:
        self.image:str = ("../assets/black_bishop.png", "../assets/white_bishop.png")[color=="black"]

    
    
class King():
    def __init__(self, color:str) -> None:
        self.image:str = ("../assets/black_king.png", "../assets/white_king.png")[color=="black"]

