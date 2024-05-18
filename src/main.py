import pygame as pg
from view import *
from terrain import *
from img import *
# import pygame_gui as pg_gui


def main():
    print("Hello World")
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Pinglouin")
    screen.fill((0, 100, 100))
    pg.display.flip()
    
    images = Images()
    
    view = View(screen, images)
    tiles = Terrain.test(images)
    tiles[2][1].rotate(False)
    tiles[2][1].rotate(False)
    tiles[1][1].rotate(False)

    clock = pg.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0
        
        events = pg.event.get()
        pressed = pg.key.get_pressed()
        
        for event in events:
            if event.type == pg.QUIT or pressed[pg.K_ESCAPE]:
                is_running = False
            
        view.draw(tiles)
        
    


if __name__=="__main__":
    main()