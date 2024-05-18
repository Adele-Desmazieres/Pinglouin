# la vue

import pygame as pg
from pingu import Pingu
from water import Water

class View:
    def __init__(self, screen, images):
        self.screen = screen
        self.images = images

    def scale_sprites(self, image, scale):
        return pg.transform.scale_by(image,(scale,scale))
    
    def draw(self, tiles, scale, pingu, water, win=False):        
        plateau = pg.Surface((780, 580))
        if win: 
            self.screen.fill((50, 157, 178))
            plateau.fill((50, 157, 178))
        else:
            self.screen.fill((176, 117, 78))
            plateau.fill((176, 117, 78))
            
        tilewidth = 32
        tileheigth = 32
        tilespace = 1
        for i in range(len(tiles)):
            for j in range(len(tiles[0])):
                img = tiles[i][j].draw()
                plateau.blit(img, (i*(tilewidth+tilespace), j*(tileheigth+tilespace), tilewidth, tileheigth))
        
        plateau.blit(pingu.draw(), (pingu.x*(32+tilespace), pingu.y*(32+tilespace)-8))
        plateau.blit(water.img, (water.x*(32+tilespace), water.y*(32+tilespace)))
        
        plateau = self.scale_sprites(plateau, scale)
        self.screen.blit(plateau, (0, 0))
        pg.display.flip()
        