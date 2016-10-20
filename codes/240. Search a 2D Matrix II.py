# class Solution(object):
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if not matrix:
#             return False
        
#         x = 0
#         y = len(matrix[0]) - 1
        
#         while x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]):
#             if matrix[x][y] == target:
#                 return True
#             elif matrix[x][y] < target:
#                 x += 1
#             else:
#                 y -= 1
            
#         return False

class Solution(object):
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		if not matrix: return False

		return self.search(matrix, target, 0, 0, len(matrix), len(matrix[0]))

	def search(self, matrix, target, x1, y1, x2, y2):
		if x1 >= x2 or y1 >= y2: return False
		if matrix[x1][y1] > target or matrix[x2 - 1][y2 - 1] < target:
			return False

		if matrix[x1][y1] == target:
			return True

		midx = (x1 + x2) / 2
		midy = (y1 + y2) / 2
		if self.search(matrix, target, x1, y1, midx, midy)\
			or self.search(matrix, target, midx, y1, x2, midy)\
			or self.search(matrix, target, x1, midy, midx, y2)\
			or self.search(matrix, target, midx, midy, x2, y2):
				return True

		return False
