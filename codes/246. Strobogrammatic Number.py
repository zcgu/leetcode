# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Write a function to determine if a number is strobogrammatic. The number is represented as a string.

# For example, the numbers "69", "88", and "818" are all strobogrammatic.

# Show Company Tags
# Show Tags
# Show Similar Problems


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num: return False
        
        for n in num:
            if n in ['2', '3', '4', '5', '7']:
                return False
        
        table = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        num2 = ''
        for n in num:
            num2 += table[n]
        
        return num == num2[::-1]
