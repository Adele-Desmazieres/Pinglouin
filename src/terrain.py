from enum import Enum
from img import Images
from direction import PathType

class Dir(Enum): # directions
    nbr = 4
    
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    
    def rotate(dir, right=True):
        if right:
            return (dir + 1) % Dir.nbr
        else:
            return (dir - 1) % Dir.nbr

class Tile:
    
    def __init__(self, pathtype, images):
        self.pathtype = pathtype
        self.connections = [] # list of list of Dirs
        self.img = images.get_tile_img(self.pathtype)
        self.rot = 0 # rotation
        match pathtype:
            case PathType.O:
                self.connections = []
            case PathType.I:
                self.connections = [[Dir.NORTH, Dir.SOUTH]]
            case PathType.L:
                self.connections = [[Dir.NORTH, Dir.EAST]]
            case PathType.T:
                self.connections = [[Dir.WEST, Dir.SOUTH, Dir.EAST]]
            case PathType.X:
                self.connections = [[Dir.WEST, Dir.EAST, Dir.NORTH, Dir.SOUTH]]
            case PathType.P:
                self.connections = [[Dir.WEST, Dir.EAST], [Dir.NORTH, Dir.SOUTH]]
            case PathType.H:
                self.connections = [[Dir.WEST, Dir.NORTH], [Dir.EAST, Dir.SOUTH]]
    
    def rotate(self, right=True):
        self.rot = (self.rot + 1) % Dir.nbr
        for i in range(self.connections):
            for j in range(self.connections[i]):
                self.connections[i][j] = Dir.rotate(self.connections[i][j], right)
        return self.connections
        
    def draw(self):
        # print("THERE ")
        # print(self.img)
        return self.img



class Terrain:
    
    def __init__(self, tiles):
        self.tiles = tiles
    
    def from_pathtypes(pathtypes, images):
        tiles = [[None for j in range(len(pathtypes[i]))] for i in range(len(pathtypes))]
        for i in range(len(pathtypes)):
            for j in range(len(pathtypes[i])):
                tiles[i][j] = Tile(pathtypes[i][j], images)
        return tiles
    
    def test(images):
        O = PathType.O
        I = PathType.I
        L = PathType.L
        T = PathType.T
        X = PathType.X
        P = PathType.P
        H = PathType.H
        
        map = [[X, O, O], 
               [L, I, L], 
               [O, O, X]]
        map = [[map[j][i] for j in range(len(map[i]))] for i in range(len(map))]
        return Terrain.from_pathtypes(map, images)
