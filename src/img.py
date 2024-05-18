import pygame as pg
import math
from pathtype import PathType

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
        self.sprite_tiles  = pg.image.load("../img/sprites.png")
        columns = 3
        
        self.sprite_O = Images.get_sprite_at(self.sprite_tiles, 0, columns)
        self.sprite_I = Images.get_sprite_at(self.sprite_tiles, 1, columns)
        self.sprite_L = Images.get_sprite_at(self.sprite_tiles, 2, columns)
        self.sprite_T = Images.get_sprite_at(self.sprite_tiles, 3, columns)
        self.sprite_X = Images.get_sprite_at(self.sprite_tiles, 4, columns)
        self.sprite_P = Images.get_sprite_at(self.sprite_tiles, 6, columns)
        self.sprite_H = Images.get_sprite_at(self.sprite_tiles, 7, columns)
        
        self.sprite_pingu1 = Images.get_sprite_at(self.sprite_tiles, 8, columns)
        self.sprite_pingu2 = Images.get_sprite_at(self.sprite_tiles, 9, columns)

        self.sprite_water = Images.get_sprite_at(self.sprite_tiles, 10, columns)
    
    def get_tile_img(self, pathtype):
        
        match pathtype:
            case PathType.O: return self.sprite_O
            case PathType.I: return self.sprite_I
            case PathType.L: return self.sprite_L
            case PathType.T: return self.sprite_T
            case PathType.X: return self.sprite_X
            case PathType.P: return self.sprite_P
            case PathType.H: return self.sprite_H
    
    def get_sprite_at(img, n, columns):
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
    
    def rot_center(image, angle):
        rotated_image = pg.transform.rotate(image, angle)
        # new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)
        return rotated_image