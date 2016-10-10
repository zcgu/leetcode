# Implement an iterator to flatten a 2d vector.

# For example,
# Given 2d vector =

# [
#   [1,2],
#   [3],
#   [4,5,6]
# ]
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.x = 0
        self.y = 0
        self.m = vec2d

        while self.x < len(self.m) and self.y >= len(self.m[self.x]):
            self.x += 1
            self.y = 0
        
    def next(self):
        """
        :rtype: int
        """
        num = self.m[self.x][self.y]
        
        self.y += 1
        while self.x < len(self.m) and self.y >= len(self.m[self.x]):
            self.x += 1
            self.y = 0
        
        return num
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.x < len(self.m) and self.y < len(self.m[self.x])

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
