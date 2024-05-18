from pathtype import PathType
from terrain import Terrain
from pingu import Pingu
from water import Water

O = PathType.O
I = PathType.I
L = PathType.L
T = PathType.T
X = PathType.X
P = PathType.P
H = PathType.H

class LevelManager:
    
    def __init__(self, images):
        self.levels = [Level(), Level(), Level(), Level()]
        self.levels[0].level_1(images)
        self.levels[1].level_2(images)
        self.levels[2].level_3(images)
        self.levels[3].level_4(images)
        self.curr_level = 0
    
    def next_level(self):
        self.curr_level += 1
        if (self.curr_level) >= len(self.levels):
            print("VICTOIRE !")
            self.curr_level = 0
    
    def get_curr_level(self):
        return self.levels[self.curr_level]
    
    def get_tiles(self, images):
        lvl = self.get_curr_level()
        return Terrain.from_pathtypes(lvl.map, lvl.rotation_map, images)


class Level:
    
    def __init__(self):
        self.map = None
        self.rotation_map = None

        self.start = (0,0)
        self.end = (1,1)

    def level_1(self, images):
        self.map = [[O, O, O, O, O],
                    [O, O, O, O, O],
                    [I, I, I, I, X],
                    [O, O, O, O, O],
                    [O, O, O, O, O]]
        
        self.rotation_map = [[0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [1, 1, 0, 1, 1],
                             [0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0]]
        
        self.start = (0,2)
        self.end = (4,2)

        self.map = Terrain.transpose_arr(self.map)
        self.rotation_map = Terrain.transpose_arr(self.rotation_map)

        return Terrain.from_pathtypes(self.map, self.rotation_map, images)
    
    def level_2(self, images):
        self.map = [[X, I, T, I, L],
                    [I, O, I, O, I],
                    [I, I, I, I, O],
                    [L, I, T, I, X],
                    [O, O, O, O, O]]
        
        self.rotation_map = [[0, 0, 2, 1, 0],
                             [0, 0, 0, 0, 0],
                             [1, 1, 0, 1, 1],
                             [0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0]]
        
        self.start = (0,0)
        self.end = (4,3)

        self.map = Terrain.transpose_arr(self.map)
        self.rotation_map = Terrain.transpose_arr(self.rotation_map)

        return Terrain.from_pathtypes(self.map, self.rotation_map, images)
    
    def level_3(self, images):
        self.map = [[X, L, L, I, X],
                    [I, I, I, L, L],
                    [I, I, I, I, O],
                    [I, L, T, L, X],
                    [L, I, O, O, O]]
        
        self.rotation_map = [[0, 0, 2, 1, 0],
                             [0, 0, 0, 0, 0],
                             [1, 1, 0, 1, 1],
                             [0, 0, 0, 0, 0],
                             [0, 1, 0, 0, 0]]
        
        self.start = (0,0)
        self.end = (4,3)

        self.map = Terrain.transpose_arr(self.map)
        self.rotation_map = Terrain.transpose_arr(self.rotation_map)

        return Terrain.from_pathtypes(self.map, self.rotation_map, images)
    
    def level_4(self, images):
        self.map = [[O, X, O],
                    [O, I, O],
                    [O, X, O]]
        
        self.rotation_map = [[0, 0, 0],
                             [0, 1, 0],
                             [0, 0, 0]]
        
        self.start = (1,0)
        self.end = (1,2)

        self.map = Terrain.transpose_arr(self.map)
        self.rotation_map = Terrain.transpose_arr(self.rotation_map)

        return Terrain.from_pathtypes(self.map, self.rotation_map, images)
    
    def get_pingu(self, images):
        return Pingu(self.start[0], self.start[1], images)
    
    def get_water(self, images):
        return Water(self.end[0], self.end[1], images)