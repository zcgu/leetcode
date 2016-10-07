class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 维护一个lst，对于每一个num，如果大于最大值，插入后面，不然替换正好比他大的那个。
        
        lst = []
        
        for num in nums:
            index = self.binarySearch(lst, num)
            
            if index >= len(lst):
                lst.append(num)
            else:
                lst[index] = num
        
        return len(lst)
    
    # 找插入位置
    def binarySearch(self, lst, num):
        l = 0
        r = len(lst)
        
        while l < r:
            mid = (l + r) / 2
            
            if lst[mid] == num:
                return mid
            elif lst[mid] < num:
                l = mid + 1
            else:
                r = mid
        
        return l
        