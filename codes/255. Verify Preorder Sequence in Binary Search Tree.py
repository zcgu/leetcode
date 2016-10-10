# Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

# You may assume each number in the sequence is unique.

# Follow up:
# Could you do it using only constant space complexity?


class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        # 10, 5, 3, 7, 15, 12, 20
        
        stack = []
        lower = float('-inf')   # 这个lower比较精髓
        for num in preorder:
            if not stack:
                stack.append(num)
            else:
                if num < lower:
                    return False
                    
                while stack and num > stack[-1]:
                    lower = stack.pop()
                
                stack.append(num)
        return True
        
        
    #     return self.dfs(preorder)
        
    # def dfs(self, lst):
    #     if not lst: return True
        
    #     num = lst[0]
    #     index = -1
    #     for i in range(1, len(lst)):
    #         if lst[i] > num and index == -1:
    #             index = i
    #         if lst[i] < num and index != -1:
    #             return False
    #     if index == -1: index = len(lst)
        
    #     if not self.dfs(lst[1:index]) or not self.dfs(lst[index:]):
    #         return False
        
    #     return True
        
