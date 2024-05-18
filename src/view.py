# la vue

import pygame as pg

class View:
    def __init__(self, screen, images):
        self.screen = screen
        self.images = images
    
    def draw(self, tiles):
        
        plateau = pg.Surface((780, 580))
        tilewidth = 32
        tileheigth = 32
        for i in range(len(tiles)):
            for j in range(len(tiles[0])):
                img = tiles[i][j].draw()
                plateau.blit(img, (i*tilewidth, j*tileheigth, tilewidth, tileheigth))
                
        self.screen.blit(plateau, (10, 10))
        pg.display.flip()
        