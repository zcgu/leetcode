class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
            
        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    res += 1
                    self.clean(grid, x, y)
        return res
    
    def clean(self, grid, x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return
        if grid[x][y] == '0':
            return
        grid[x][y] = '0'
        for i, j in [[-1, 0], [1,0], [0,1], [0,-1]]:
            self.clean(grid, x+i, y+j)