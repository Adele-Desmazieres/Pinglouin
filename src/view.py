# la vue

import pygame as pg

class View:
    def __init__(self, screen, images):
        self.screen = screen
        self.images = images
    
    def draw(self, tiles, scale):
        
        plateau = pg.Surface((780, 580))
        tilewidth = 32
        tileheigth = 32
        tilespace = 1
        for i in range(len(tiles)):
            for j in range(len(tiles[0])):
                img = tiles[i][j].draw()
                plateau.blit(img, (i*(tilewidth+tilespace), j*(tileheigth+tilespace), tilewidth, tileheigth))
                
        if scale == 2:
            plateau = pg.transform.scale2x(plateau)
        elif scale == 3:
            plateau = pg.transform.smoothscale_by(plateau,(scale,scale))
        self.screen.blit(plateau, (10, 10))
        pg.display.flip()
        