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
    

# to find the path from
# top left to bottom right
def get_shortest_path(arr, start, end) :
    # the values for our future path are at -1
    path_values = [[-1]*len(arr)]*len(arr[0])
    
    # queue
    final_path = []
    
    path_values[end[0]][end[1]] = 0
    number_loop = len(arr)*len(arr[0])

    while path_values[start[0]][start[1]] == -1 and number_loop > 0:
        for i in range(len(arr)-1):
            for j in range(len(arr[0])-1):
                if arr[i][j] != 0:
                    value = path_values[i][j] + 1
                    if check_connections_left_right(arr[i][j], arr[i][j+1]):                    
                        if path_values[i][j+1] > value:
                            path_values[i][j+1] = value
                    if check_connections_up_down(arr[i][j], arr[i+1][j]):
                        if path_values[i+1][j] > value:
                            path_values[i+1][j] = value
                else:
                    path_values[i][j] = -1
        number_loop -= 1
    
    final_path.append(start)
    last_value = path_values[start[0]][start[1]]
    while last_value != 0:
        if path_values[start[0]+1][start[1]] == last_value-1 or path_values[start[0]][start[1]+1] == last_value-1:
            final_path.append((start[0]+1, start[1]))
            start = (start[0]+1, start[1])

    return final_path

# Given array
# arr =  [[ 4, 4, 4, 4, 4 ],
#         [ 0, 0, 0, 0, 4 ],
#         [ 0, 0, 0, 0, 4 ],
#         [ 0, 0, 0, 0, 4 ],
#         [ 0, 0, 0, 0, 4 ]]

# # path from arr[0][0] to arr[row][col]
# # print(get_shortest_path(arr, (0, 0), (row-1, col-1)))

# print(check_connections_left_right(Tile(PathType.I), Tile(PathType.X)))

