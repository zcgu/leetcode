class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        tmp = []
        
        for num in nums:
            if not tmp or num > tmp[-1][-1] + 1:
                tmp.append([num])
            elif len(tmp[-1]) == 1:
                tmp[-1].append(num)
            else:
                tmp[-1][-1] = num
        
        res = [str(pair[0]) + '->' + str(pair[1]) if len(pair) == 2 else str(pair[0]) for pair in tmp]
        return res