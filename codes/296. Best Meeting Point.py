# A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

# For example, given three people living at (0,0), (0,4), and (2,2):

# 1 - 0 - 0 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.

# Show Hint 
# Show Company Tags
# Show Tags
# Show Similar Problems


class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        
        total = sum(grid[x][y] 
                    for x in range(len(grid))
                    for y in range(len(grid[0])))
        
        i = -1
        num = 0
        for x in range(len(grid)):
            num += sum(grid[x])
            if num > total / 2:
                i = x
                break
        
        j = -1
        num = 0
        for y in range(len(grid[0])):
            num += sum(grid[x][y] for x in range(len(grid)))
            if num > total / 2:
                j = y
                break
        print i, j
        return sum(abs(i - x) + abs(j - y)
                    for x in range(len(grid))
                    for y in range(len(grid[0]))
                    if grid[x][y] == 1)


