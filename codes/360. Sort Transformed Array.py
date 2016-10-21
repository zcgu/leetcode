# Given a sorted array of integers nums and integer values a, b and c. Apply a function of the form f(x) = ax2 + bx + c to each element x in the array.

# The returned array must be in sorted order.

# Expected time complexity: O(n)

# Example:
# nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

# Result: [3, 9, 15, 33]

# nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

# Result: [-23, -5, 1, 7]
# Credits:
# Special thanks to @elmirap for adding this problem and creating all test cases.

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        # 这题a有好多情况，好烦
        sign = 1 if a >= 0 else -1
        
        def f(x):
            return a * x * x + b * x + c

        p1 = 0
        p2 = len(nums) - 1
        res = []

        while p1 <= p2:
            num1 = f(nums[p1])
            num2 = f(nums[p2])
            if sign * num1 > sign * num2:
                if sign == 1:
                    res.insert(0, num1)
                else:
                    res.append(num1)
                p1 += 1
            else:
                if sign == 1:
                    res.insert(0, num2)
                else:
                    res.append(num2)
                p2 -= 1

        return res
        
    
  


