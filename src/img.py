import pygame as pg
from direction import PathType

class Images:
    sprite_O = pg.image.load("tile_o.png")
    sprite_I = pg.image.load("tile_i.png")
    sprite_L = pg.image.load("tile_l.png")
    sprite_T = pg.image.load("tile_t.png")
    sprite_X = pg.image.load("tile_x.png")
    sprite_P = pg.image.load("tile_p.png")
    sprite_H = pg.image.load("tile_h.png")

    def __init__(self):
        broken = pg.image.load("broken.png")
    
    def get_tile_img(self, pathtype):
        match pathtype:
            case PathType.O: return sprite_O
            case PathType.I: return sprite_I
            case PathType.L: return sprite_L
            case PathType.T: return sprite_T
            case PathType.X: return sprite_X
            case PathType.P: return sprite_P
            case PathType.H: return sprite_H
