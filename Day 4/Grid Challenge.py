import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    for row in range(len(grid)):
        grid[row] = sorted(grid[row])
        
    for col in range(len(grid[0])):  
        col_list = [row[col] for row in grid]
        
        print(col_list, sorted(col_list))
        print(col_list != sorted(col_list))

        if col_list != sorted(col_list):
            return 'NO'
        
    return 'YES'

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()