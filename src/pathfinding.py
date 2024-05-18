from terrain import *

row = 5
col = 5

def check_connections_up_down(tile_up, tile_down):
    tile_up_ok = False
    tile_down_ok = False
    for i in range(len(tile_down.connections)):
        if Dir.NORTH in tile_down.connections[i]:
            tile_down_ok = True
    for i in range(len(tile_up.connections)):
        if Dir.SOUTH in tile_up.connections[i]:
            tile_up_ok = True
    return tile_down_ok and tile_up_ok
    
def check_connections_left_right(tile_left, tile_right):
    tile_left_ok = False
    tile_right_ok = False
    for i in range(len(tile_left.connections)):
        if Dir.EAST in tile_left.connections[i]:
            tile_left_ok = True
    for i in range(len(tile_right.connections)):
        if Dir.WEST in tile_right.connections[i]:
            tile_right_ok = True
    return tile_right_ok and tile_left_ok


def print_matrix(m):
    print("[")
    for i in range(len(m)):
        print(m[i])
    print("]")

# returns a boolean, true if a path is found from begin to end
def has_shortest_path(tiles, start, end) :
    h = len(tiles)
    w = len(tiles[0])
    
    max = w * h + 1
    
    
    # the values for our future path are at -1
    path_values = [[max for x in range(h)] for y in range(w)]
    # init with 0 at the end
    path_values[end[0]][end[1]] = 0
    # print_matrix(path_values)
    path_values = [[max] * w] + path_values + [[max] * w]
    # print_matrix(path_values)
    path_values = [[max] + x + [max] for x in path_values]
    # print_matrix(path_values)
    # print(path_values)
    
    
    # chemin
    # final_path = []
    number_loop = h * w

    # évaluer les distances
    while path_values[start[0]][start[1]] == max and number_loop > 0:
        
        for i in range(1, h):
            for j in range(1, w):
                
                tile = tiles[i-1][j-1]
                v = path_values[i][j]
                
                if path_values[i-1][j] != max:
                    if check_connections_left_right(tiles[i-1-1][j-1], tile):
                        v = min(v, path_values[i-1][j]+1)
                
                if path_values[i+1][j] != max:
                    if check_connections_left_right(tile, tiles[i+1-1][j-1]):
                        v = min(v, path_values[i+1][j]+1)
                
                if path_values[i][j-1] != max:
                    if check_connections_up_down(tiles[i-1][j-1-1], tile):
                        v = min(v, path_values[i][j-1]+1)

                if path_values[i][j+1] != max:
                    if check_connections_up_down(tiles[i-1][j+1-1], tile):
                        v = min(v, path_values[i][j+1]+1)
                
                path_values[i][j] = v
        
        number_loop -= 1
    
    # print_matrix(path_values)
    path_found = (path_values[start[0]+1][start[1]+1] != max)
    # print(start[0]+1, start[1]+1)
    # print(path_found)
    return path_found

# Given array
# arr =  [[ 4, 4, 4, 4, 4 ],
#         [ 0, 0, 0, 0, 4 ],
#         [ 0, 0, 0, 0, 4 ],
#         [ 0, 0, 0, 0, 4 ],
#         [ 0, 0, 0, 0, 4 ]]

# # path from arr[0][0] to arr[row][col]
# # print(get_shortest_path(arr, (0, 0), (row-1, col-1)))

# print(check_connections_left_right(Tile(PathType.I), Tile(PathType.X)))

