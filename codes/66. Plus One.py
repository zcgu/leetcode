class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        
        for i in range(len(digits) - 1, -1, -1):
            num = digits[i] + carry
            digits[i] = num % 10
            carry = num / 10
        
        if carry == 1:
            digits.insert(0, 1)
        
        return digits
        