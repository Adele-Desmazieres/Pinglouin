# la vue

import pygame as pg

class View:
    def __init__(self, screen, images):
        self.screen = screen
        self.images = images

    def scale_sprites(self, image, scale):
        return pg.transform.scale_by(image,(scale,scale))
    
    def draw(self, tiles, scale, pingu):        
        plateau = pg.Surface((780, 580))
        tilewidth = 32
        tileheigth = 32
        tilespace = 1
        for i in range(len(tiles)):
            for j in range(len(tiles[0])):
                img = tiles[i][j].draw()
                plateau.blit(img, (i*(tilewidth+tilespace), j*(tileheigth+tilespace), tilewidth, tileheigth))
                
        plateau = self.scale_sprites(plateau, scale)
        self.screen.blit(plateau, (10, 10))
        
        pingu = self.scale_sprites(pingu.draw(), scale)
        self.screen.blit(pingu, (10, 10))
        
        pg.display.flip()
        