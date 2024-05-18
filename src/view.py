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
        
        if not win:
            plateau.blit(pingu.draw(), (pingu.x*(32+tilespace), pingu.y*(32+tilespace)-8))
            
        plateau.blit(water.draw(win), (water.x*(32+tilespace), water.y*(32+tilespace)))
        
        plateau = self.scale_sprites(plateau, scale)
        self.screen.blit(plateau, (0, 0))
        pg.display.flip()

    # Fonction pour afficher le message de victoire
    def show_victory_screen(self):
        # Couleurs
        white = (255, 255, 255)
        black = (0, 0, 0)
        green = (0, 255, 0)

        # Police de caractères
        font = pg.font.SysFont(None, 75)
        font2 = pg.font.SysFont(None, 50)

        self.screen.fill((50, 157, 178))
        victory_text = font.render("Victoire !", True, black)
        text = font2.render("Appuyez sur une touche pour rejouer", True, black)
        self.screen.blit(victory_text, (self.screen.get_width() // 4, self.screen.get_height() // 2))
        self.screen.blit(text, (0, self.screen.get_height() // 2 + 50))
        pg.display.flip()

        # Attendre que l'utilisateur appuie sur une touche ou ferme la fenêtre
        waiting = True
        while waiting:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

                if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
                    waiting = False
        