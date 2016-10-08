class MyNode:
    def __init__(self, start, end, sums):
        self.start = start
        self.end = end
        self.sums = sums
        
        self.left = None
        self.right = None

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.root = self.buildTree(nums, 0, len(nums) - 1)
    
    def buildTree(self, nums, start, end):
        if start > end:
            return None
            
        node = MyNode(start, end, sum(nums[start: end+1]))
        
        if start != end:
            node.left = self.buildTree(nums, start, (start + end) / 2)
            node.right = self.buildTree(nums, (start + end) / 2 + 1, end)
        
        return node

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.updateHelper(self.root, i, val)
        self.nums[i] = val
        
        
        
    def updateHelper(self, node, i, val):
        if not node:
            return
        
        node.sums = node.sums - self.nums[i] + val
        
        if i <= (node.start + node.end) / 2:
            self.updateHelper(node.left, i, val)
        else:
            self.updateHelper(node.right, i, val)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.getSum(self.root, i, j)
        
        
    def getSum(self, node, i, j):
        if i == node.start and j == node.end:
            return node.sums
        
        elif j <= (node.start + node.end) / 2:
            return self.getSum(node.left, i, j)
        
        elif i > (node.start + node.end) / 2:
            return self.getSum(node.right, i, j)
        
        else:
            return self.getSum(node.left, i, node.left.end) + self.getSum(node.right, node.right.start, j)


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)