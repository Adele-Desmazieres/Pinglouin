import pygame as pg
from view import *
from terrain import *
from img import Images
from pingu import Pingu
from level import Level, LevelManager
import pathfinding
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
    screen.fill((176, 117, 78))
    pg.display.flip()
    
    images = Images()
    
    view = View(screen, images)

    # Level selection
    lvls = LevelManager(images)
    # tiles = level.level_1(images)
    tiles = lvls.get_tiles(images)
    lvl = lvls.get_curr_level()
    pingu = lvl.get_pingu(images)
    water = lvl.get_water(images)

    clock = pg.time.Clock()
    is_running = True
    while is_running:
        rotated = False
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
                        rotated = True
                except IndexError:
                    pass
    
            if rotated:
                # test du pathfinding
                haspath = pathfinding.has_shortest_path(tiles, lvl.start, lvl.end)
                if (haspath):
                    print("PATH FOUND")
                    view.draw(tiles, scale, pingu, water, True)
                    pg.time.wait(1300)
                    lvls.next_level()
                    tiles = lvls.get_tiles(images)
                    lvl = lvls.get_curr_level()
                    pingu = lvl.get_pingu(images)
                    water = lvl.get_water(images)

                    

        view.draw(tiles, scale, pingu, water, False)
        
    


if __name__=="__main__":
    main()