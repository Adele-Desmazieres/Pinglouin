import pygame as pg
import math
from direction import PathType

class Images:
    # sprite_broken = None
    # sprite_O = None
    # sprite_I = None
    # sprite_L = None
    # sprite_T = None
    # sprite_X = None
    # sprite_P = None
    # sprite_H = None

    def __init__(self):
        self.sprite_broken = pg.image.load("../img/broken.png")
        
        self.sprite_tiles  = pg.image.load("../img/sand3.png")
        self.sprite_O = Images.get_sprite_at(self.sprite_tiles, 0, 8, 1)
        self.sprite_I = Images.get_sprite_at(self.sprite_tiles, 1, 8, 1)
        self.sprite_L = Images.get_sprite_at(self.sprite_tiles, 2, 8, 1)
        self.sprite_T = Images.get_sprite_at(self.sprite_tiles, 3, 8, 1)
        self.sprite_X = Images.get_sprite_at(self.sprite_tiles, 4, 8, 1)
        self.sprite_P = Images.get_sprite_at(self.sprite_tiles, 6, 8, 1)
        self.sprite_H = Images.get_sprite_at(self.sprite_tiles, 7, 8, 1)
    
    def get_tile_img(self, pathtype):
        
        match pathtype:
            case PathType.O: return self.sprite_O
            case PathType.I: return self.sprite_I
            case PathType.L: return self.sprite_L
            case PathType.T: return self.sprite_T
            case PathType.X: return self.sprite_X
            case PathType.P: return self.sprite_P
            case PathType.H: return self.sprite_H
    
    def get_sprite_at(img, n, columns, lines):
        sprite_heigth = 32
        sprite_width = 32
        # y = math.floor((sprite_heigth * n) / (columns*sprite_heigth))
        # x = (sprite_width * n) % (columns*sprite_width)
        y = n // columns
        x = n % columns
        portion_rect = pg.Rect(x*sprite_width, y*sprite_heigth, sprite_width, sprite_heigth)
        # portion_rect = pg.Rect(32, 0, sprite_width, sprite_heigth)
        image_portion = img.subsurface(portion_rect).copy()
        
        return image_portion
