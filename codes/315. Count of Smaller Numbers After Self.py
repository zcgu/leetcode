class Mynode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1   # size

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        
        root = Mynode(nums[-1])
        
        res = [0]
        
        for num in reversed(nums[:-1]):
            res.insert(0, self.insert(root, num))
            
        return res
        
        
    def insert(self, root, num):
        # print root.val, num
        root.size += 1
        if num <= root.val:
            if root.left:
                return self.insert(root.left, num)
            else:
                root.left = Mynode(num)
                return 0
        else:
            if root.right:
                return (root.left.size if root.left else 0) + 1\
                    + self.insert(root.right, num)
            else:
                root.right = Mynode(num)
                return (root.left.size if root.left else 0) + 1
                

            