# You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
# For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):

# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.

# Note:
# There will be at least one building. If it is not possible to build such house according to the above rules, return -1.


class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        
        m = len(grid)
        n = len(grid[0])

        totalb = 0
        reach = [[0 for _ in range(n)] for _ in range(m)]
        totald = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited = [[False for l in range(n)] for k in range(m)]
                                        
                    que = [(i, j, 0)]

                    while que:
                        x, y, d = que.pop(0)
                        if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or \
                            (d != 0 and grid[x][y] == 1 or grid[x][y] == 2) :
                            continue
                        
                        visited[x][y] = True
                        reach[x][y] += 1
                        totald[x][y] += d
                        for xx, yy in[(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                            que.append((xx, yy, d + 1))
                    
                    totalb += 1
        
        res = 2 ** 31 - 1
        row = col = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0 and reach[x][y] == totalb and totald[x][y] < res:
                    row, col, res = x, y, totald[x][y]
        return res if res < 2 ** 31 - 1 else -1

