# A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example:

# Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

# 0 0 0
# 0 0 0
# 0 0 0
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
# We return the result as an array: [1, 1, 2, 3]

# Challenge:

# Can you do it in time complexity O(k log mn), where k is the length of the positions?


class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        
        tree = [[None for y in range(n)] 
                for x in range(m)]
        count = 0
        res = []
        
        for p in positions:
            x, y = p[0], p[1]
            if tree[x][y] is not None:
                res.append(count)
                continue
    
            tree[x][y] = (x, y)
            count += 1
            for xx, yy in [(x + 1, y), (x-1,y), (x, y+1), (x, y-1)]:
                root = self.find(tree, xx, yy)
                if root and root != (x, y):
                    tree[root[0]][root[1]] = (x, y)
                    count -= 1
            
            res.append(count)
        
        return res


    def find(self, tree, x, y):



        if x < 0 or x >= len(tree) or y < 0 or y >= len(tree[0]) or not tree[x][y]:
            return None
        
        while tree[x][y] != (x, y):
            tree[x][y] = tree[tree[x][y][0]][tree[x][y][1]]        # trick
            x, y  = tree[x][y]
        
        return x, y

