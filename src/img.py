import pygame as pg
from terrain import PathType

class Images:

    def __init__(self):
        broken = pg.image.load("broken.png")
    
    def get_tile_img(self, pathtype):
        match pathtype:
            case PathType.O: return pg.image.load("tile_o.png")
            case PathType.I: return pg.image.load("tile_i.png")
            case PathType.L: return pg.image.load("tile_l.png")
            case PathType.T: return pg.image.load("tile_t.png")
            case PathType.X: return pg.image.load("tile_x.png")
            case PathType.P: return pg.image.load("tile_p.png")
            case PathType.H: return pg.image.load("tile_h.png")
