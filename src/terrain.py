import math
from enum import IntEnum
from img import Images
from direction import PathType

DIRNBR = 4

class Dir(IntEnum): # directions
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    
    def rotate(dir, right=True):
        if right:
            return (dir + 1) % DIRNBR
        else:
            return (dir - 1) % DIRNBR
    
    def to_angle(dir):
        match dir:
            case Dir.NORTH: return math.pi / 2
            case Dir.EAST: return 0.0
            case Dir.SOUTH: return 3 * math.pi / 2
            case Dir.WEST: return math.pi
    
    
class Tile:
    
    def __init__(self, pathtype, images):
        self.pathtype = pathtype
        self.connections = [] # list of list of Dirs
        self.img = images.get_tile_img(self.pathtype)
        self.img_rot = self.img.copy()
        self.rot = 0 # rotation as int corresponding to directions
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
        if right:
            self.rot = (self.rot + 1) % DIRNBR
        else:
            self.rot = (self.rot - 1) % DIRNBR
        for i in range(len(self.connections)):
            for j in range(len(self.connections[i])):
                self.connections[i][j] = Dir.rotate(self.connections[i][j], right)
        angle_deg = math.degrees(Dir.to_angle(self.rot) - math.pi/2) # minus north default orientation
        self.img_rot = Images.rot_center(self.img, angle_deg)
    
    def set_rotation(self, rot):
        if self.rot < rot:
            i = self.rot
            fin = rot
            right = True
        else:
            i = rot
            fin = self.rot
            right = False
        while i < fin:
            self.rotate(right)
            i += 1
    
    def draw(self):
        return self.img_rot



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
