from enum import Enum

class PathType(Enum):
    O = 0 # pas de chemin
    I = 1
    L = 2
    T = 3
    X = 4 # croisement
    P = 5 # pont N-S et E-W
    H = 6 # pont N-W et S-E


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
        self.connections = [] # list of list of Dir
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
        for i in range(self.connections):
            for j in range(self.connections[i]):
                self.connections[i][j] = Dir.rotate(self.connections[i][j], right)
        return self.connections
    
    # def draw(self):


class Terrain:
    
    def __init__(self, tiles):
        self.tiles = tiles