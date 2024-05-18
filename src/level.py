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
        pass

    def niveau_1(images):
        map = [[O, O, O, O, O],
               [O, O, O, O, O],
               [I, I, I, I, I],
               [O, O, O, O, O],
               [O, O, O, O, O]]
        
        rotation_map = [[0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [1, 1, 0, 1, 1],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]]
        map = [[map[j][i] for j in range(len(map[i]))] for i in range(len(map))]
        rotation_map = [[rotation_map[j][i] for j in range(len(rotation_map[i]))] for i in range(len(rotation_map))]

        return Terrain.from_pathtypes(map, rotation_map, images)