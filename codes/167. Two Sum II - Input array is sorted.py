class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) <= 1:
            return [0, 0]
        
        p1 = 0
        p2 = len(numbers) - 1
        
        while p1 < p2:
            if numbers[p1] + numbers[p2] == target:
                return [p1 + 1, p2 + 1]
        
            if numbers[p1] + numbers[p2] < target:
                p1 += 1
            else:
                p2 -= 1