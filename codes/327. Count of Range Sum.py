class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sums = [0] + [sum(nums[:i+1]) for i in range(len(nums))]
        # print sums
        return self.mergeSort(sums, lower, upper)[1]
        
        
    def mergeSort(self, sums, lower, upper):
        # print sums
        if len(sums) <= 1:
            return sums, 0
        
        count = 0
        left, count1 = self.mergeSort(sums[:len(sums)/2], lower, upper)
        right, count2 = self.mergeSort(sums[len(sums)/2:], lower, upper)
        
        p1 = p2 = 0
        for l in left:                                                      # 右边sums减左边sums在范围内的个数。
            while p1 < len(right) and right[p1] - l < lower: p1 += 1
            while p2 < len(right) and right[p2] - l <= upper: p2 += 1
            count += p2 - p1
            # print sums, l, p1, p2, count
        
        i = j = 0
        res = []
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        res += left[i:]
        res += right[j:]
        
        return res, count1 + count2 + count
