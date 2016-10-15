# Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

# Example 1:
# Given points = [[1,1],[-1,1]], return true.

# Example 2:
# Given points = [[1,1],[-1,-1]], return false.

# Follow up:
# Could you do better than O(n2)?

# Hint:

# Find the smallest and largest x-value for all points.
# If there is a line then it should be at y = (minX + maxX) / 2.
# For each point, make sure that it has a reflected point in the opposite side.
# Credits:
# Special thanks to @memoryless for adding this problem and creating all test cases.

class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len(points) == 0: return True
        if len(points) == 1: return True

        minx = min(p[0] for p in points)
        maxx = max(p[0] for p in points)

        x = float(minx + maxx) / 2

        sets = set((p[0], p[1]) for p in points)

        for p in sets:
            if (x * 2 - p[0], p[1]) not in sets:
                return False
        return True

        

