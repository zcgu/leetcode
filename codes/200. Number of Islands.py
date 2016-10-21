class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
    
        m = len(grid)
        n = len(grid[0])
        
        tree = [[None for _ in range(n)] for _ in range(m)]
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    tree[x][y] = (x, y)
                    
                    for xx, yy in [(x + 1,y), (x-1,y), (x, y+1), (x, y-1)]:
                        root = self.findRoot(tree, xx, yy)
                        if root:
                            tree[root[0]][root[1]] = (x, y)
        
        res = 0
        for x in range(m):
            for y in range(n):
                if tree[x][y] == (x, y):
                    res += 1
        return res
        
        
    def findRoot(self, tree, x, y):
        if x < 0 or x >= len(tree) or y < 0 or y >= len(tree[0]) or not tree[x][y]: return None
        
        while (x, y) != tree[x][y]:
            tree[x][y] = tree[tree[x][y][0]][tree[x][y][1]]
            x, y = tree[x][y]
        
        return (x, y)

# class Solution(object):
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         if not grid:
#             return 0
            
#         res = 0
#         for x in range(len(grid)):
#             for y in range(len(grid[0])):
#                 if grid[x][y] == '1':
#                     res += 1
#                     self.clean(grid, x, y)
#         return res
    
#     def clean(self, grid, x, y):
#         if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
#             return
#         if grid[x][y] == '0':
#             return
#         grid[x][y] = '0'
#         for i, j in [[-1, 0], [1,0], [0,1], [0,-1]]:
#             self.clean(grid, x+i, y+j)
