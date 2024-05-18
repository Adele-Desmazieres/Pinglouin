from enum import Enum

class PathType(Enum):
    O = 0 # pas de chemin
    I = 1
    L = 2
    T = 3
    X = 4 # croisement
    P = 5 # pont N-S et E-W
    H = 6 # pont N-W et S-E
