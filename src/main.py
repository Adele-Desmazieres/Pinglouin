import pygame as pg
from view import *
from terrain import *
from img import *
from pingu import Pingu
from level import Level
# import pygame_gui as pg_gui

# Parameters
scale = 3

def is_click_inside_zone(click_pos, zone_rect, scale):
        x, y = click_pos
        rect_x, rect_y, rect_width, rect_height = zone_rect
        return rect_x <= x <= rect_x + rect_width*scale and rect_y <= y <= rect_y + rect_height*scale

def main():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Pinglouin")
    screen.fill((0, 100, 100))
    pg.display.flip()
    
    images = Images()
    level = Level()
    # pingu = Pingu(0, 0, images)
    
    view = View(screen, images)

    # Level selection
    # tiles = Terrain.test(images)
    tiles = level.level_1(images)
    pingu = Pingu(level.start[0], level.start[1], images)

    clock = pg.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0
        
        events = pg.event.get()
        pressed = pg.key.get_pressed()
        
        for event in events:
            if event.type == pg.QUIT or pressed[pg.K_ESCAPE]:
                is_running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                x = math.floor((event.pos[0]/scale))
                y = math.floor((event.pos[1]/scale))
                try:
                    if is_click_inside_zone(event.pos, (x, y, x*32, y*32), scale):
                        tiles[math.floor(x/32)][math.floor(y/32)].rotate()
                except Exception:
                    pass
        view.draw(tiles, scale, pingu)
        
    


if __name__=="__main__":
    main()