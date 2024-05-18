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
    
    def __init__(self, pathtype):
        self.pathtype = pathtype
        self.connections = [] # list of list of Dirs
        self.img = Images.get_tile_img(self.pathtype)
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
        return self.img



class Terrain:
    
    def __init__(self, tiles):
        self.tiles = tiles
    
    def from_pathtypes(pathtypes):
        tiles = [[None for j in range(len(pathtypes[i]))] for i in range(len(pathtypes))]
        for i in range(pathtypes):
            for j in range(pathtypes[i]):
                tiles[i][j] = Tile(pathtypes[i][j])
        return tiles
