class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # 先把信封按w第一排序，h第二排序（倒序），然后w没用了，然后就是最长递增子串了。
        
        
        envelopes.sort(key=lambda l: (l[0], -l[1]))
        
        nums = [e[1] for e in envelopes]
        
        lst = []
        
        for num in nums:
            if not lst or num > lst[-1]:
                lst.append(num)
                continue
            
            index = self.binarySearch(lst, num)
            
            lst[index] = num
        
        return len(lst)
    
    def binarySearch(self, lst, num):
        l = 0
        r = len(lst) - 1
        
        while l < r:
            mid = (l + r) / 2
            
            if lst[mid] == num:
                return mid
            elif lst[mid] < num:
                l = mid + 1
            else:
                r = mid
        
        return l