# Given a non-empty string str and an integer k, rearrange the string such that the same characters are at least distance k from each other.

# All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

# Example 1:
# str = "aabbcc", k = 3

# Result: "abcabc"

# The same letters are at least distance 3 from each other.
# Example 2:
# str = "aaabc", k = 3 

# Answer: ""

# It is not possible to rearrange the string.
# Example 3:
# str = "aaadbbcc", k = 2

# Answer: "abacabcd"

# Another possible answer is: "abcabcda"

# The same letters are at least distance 2 from each other.
# Credits:
# Special thanks to @elmirap for adding this problem and creating all test cases.

class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        
        from heapq import *
        heap = []
        waitque = []
        res = []
        
        for c in set(str):
            heappush(heap, (-str.count(c), c))
        
        while len(res) < len(str):
            if not heap:
                return ''

            count, c = heappop(heap)
            res += [c]
            count += 1
                                                
            waitque.append((count, c))

            if len(waitque) >= k:
                count, c = waitque.pop(0)
                if count != 0:
                    heappush(heap, (count, c))
        return ''.join(res)
