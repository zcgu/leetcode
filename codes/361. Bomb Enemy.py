# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
# Note that you can only put the bomb at an empty cell.

# Example:
# For the given grid

# 0 E 0 0
# E 0 W E
# 0 E 0 0

# return 3. (Placing a bomb at (1,1) kills 3 enemies)
# Credits:
# Special thanks to @memoryless for adding this problem and creating all test cases.


class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        m = len(grid)
        n = len(grid[0])

        value = [[0 for _ in range(n)] for _ in range(m)]

        for x in range(m):
            tmp = tmp2 = 0
            for y in range(n):
                if grid[x][y] == 'W':
                    tmp = 0
                elif grid[x][y] == 'E':
                    tmp += 1
                else:
                    value[x][y] += tmp

                if grid[x][n - 1 -y] == 'W':
                    tmp2 = 0
                elif grid[x][n - 1 -y] == 'E':
                    tmp2 += 1
                else:
                    value[x][n - 1 -y] += tmp2
        for y in range(n):
            tmp = tmp2 = 0
            for x in range(m):
                if grid[x][y] == 'W':
                    tmp = 0
                elif grid[x][y] == 'E':
                    tmp += 1
                else:
                    value[x][y] += tmp
                if grid[m-1-x][y] == 'W':
                    tmp2 = 0
                elif grid[m-1-x][y] == 'E':
                    tmp2 += 1
                else:
                    value[m-1-x][y] += tmp2

        res = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '0':
                    res = max(res, value[x][y])
        return res
