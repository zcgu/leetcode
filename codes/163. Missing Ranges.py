Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        tmp = lower
        res = []
        
        for i, num in enumerate(nums):
            if tmp > upper:
                return res
            elif num < tmp:
                pass
            elif num == tmp:
                tmp += 1
            elif num - 1 == tmp:
                res.append(str(tmp))
                tmp = num + 1
            else:
                if num - 1 >= upper:
                    res.append(str(tmp) + '->' + str(upper))
                    return res
                
                res.append(str(tmp) + '->' + str(num - 1))
                tmp = num + 1
        
        if tmp == upper:
            res.append(str(tmp))
        elif tmp < upper:
            res.append(str(tmp) + '->' + str(upper))
        return res
