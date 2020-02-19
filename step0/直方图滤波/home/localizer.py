import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    tmp_item = []
    s=0.0
    #print(grid)
    for i in range(len(grid)):
        rows = grid[i];
        for j in range(len(rows)):
            if rows[j] == color:
                tmp_item.append(beliefs[i][j]*p_hit)
            else:
                tmp_item.append(beliefs[i][j]*p_miss)
        #print('tmp_item:',tmp_item)
        s += sum(tmp_item)
        
        new_beliefs.append(tmp_item)
        tmp_item = []
    #print(s)
    
    
    for i in range(len(new_beliefs)):
        rows = new_beliefs[i]
        #print(new_beliefs[i])
        for j in range(len(rows)):
            new_beliefs[i][j] =new_beliefs[i][j]/ s
    print(new_beliefs)
    #
    # TODO - implement this in part 2
    #

    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        print("--",i,row)
        for j, cell in enumerate(row):
            new_i = (i + dy) % height
            new_j = (j + dx) % width
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)