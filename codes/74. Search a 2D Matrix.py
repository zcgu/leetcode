class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        if target < matrix[0][0]: return False
        
        l = 0
        r = len(matrix) - 1
        
        while l < r:
            mid = (l + r) / 2 + 1
            
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid
            else:
                r = mid - 1
                
        x = l
        
        l = 0
        r = len(matrix[0]) - 1
        
        while l < r:
            mid = (l + r) / 2
            
            if matrix[x][mid] == target:
                return True
            elif matrix[x][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return matrix[x][l] == target
        
        
        
        