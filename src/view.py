# la vue

import pygame as pg

class View:
    def __init__(self) -> None:
        pass
    
    def draw(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                # display(arr[i][j].)