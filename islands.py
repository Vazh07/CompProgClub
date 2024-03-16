t_map = [[1,0,0,0,1],[1,1,0,1,0],[1,0,0,0,1],[0,0,1,0,1]]


def check_for_island(t_map,i,j,islands):
    ops = [[-1,0],[1,0],[0,-1],[0,1]]
    if i<0 or i>=len(t_map) or j<0 or j>=len(t_map[0]):
        return
    if [i, j] not in islands and t_map[i][j]:
        islands.append([i, j])
        for op in ops:
            check_for_island(t_map, i+op[0], j+op[1], islands)
    else:
        return

def count_islands(t_map, islands=[]):
    s = 0
    for i, r in enumerate(t_map):
        for j, c in enumerate(r):
            if c:
                check_for_island(t_map, i, j, islands)
                print(islands)
        s += 1
        print(s)

count_islands(t_map)
