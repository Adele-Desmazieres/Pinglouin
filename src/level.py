from pathtype import PathType
from terrain import Terrain

O = PathType.O
I = PathType.I
L = PathType.L
T = PathType.T
X = PathType.X
P = PathType.P
H = PathType.H

class Level:
    def __init__(self):
        self.map = None
        self.rotation_map = None

        self.start = (0,0)
        self.end = (1,1)

    def level_1(self, images):
        self.map = [[O, O, O, O, O],
                    [O, O, O, O, O],
                    [I, I, I, I, I],
                    [O, O, O, O, O],
                    [O, O, O, O, O]]
        
        self.rotation_map = [[0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [1, 1, 0, 1, 1],
                             [0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0]]
        
        self.start = (0,2)
        self.end = (4,2)

        self.map = [[self.map[j][i] for j in range(len(self.map[i]))] for i in range(len(self.map))]
        self.rotation_map = [[self.rotation_map[j][i] for j in range(len(self.rotation_map[i]))] for i in range(len(self.rotation_map))]

        return Terrain.from_pathtypes(self.map, self.rotation_map, images)