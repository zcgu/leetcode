# An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

# For example, given the following image:

# [
#   "0010",
#   "0110",
#   "0100"
# ]
# and x = 0, y = 2,
# Return 6.

# Show Company Tags
# Show Tags


class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        lst = [max(image[i]) for i in range(len(image))]
        
        minx = self.binarySearchLeft(lst, 0 ,x)
        maxx = self.binarySearchRight(lst, x, len(lst) - 1)

        lst = ['0' for _ in range(len(image[0]))]
        for j in range(len(image[0])):
            lst[j] = max(image[i][j] for i in range(len(image)))
        
        miny = self.binarySearchLeft(lst, 0, y)
        maxy = self.binarySearchRight(lst, y, len(lst) - 1)

        return (maxx - minx + 1) * (maxy - miny + 1)

    def binarySearchLeft(self, lst, l, r):
        while l < r:
            mid = (l + r) / 2
            if lst[mid] == '0':
                l = mid + 1
            else:
                r = mid
        return l


    def binarySearchRight(self, lst, l, r):
        while l < r:
            mid = (l + r) / 2 + 1
            if lst[mid] == '0':
                r = mid - 1
            else:
                l = mid
        return l

