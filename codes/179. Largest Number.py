class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        lst = [str(num) for num in nums]
        
        lst.sort(cmp=lambda x, y: cmp(x+y, y+x), reverse=True)
        
        res = ''.join(lst)
        
        return res[:-1].lstrip('0') + res[-1]
        