# There is a fence with n posts, each post can be painted with one of the k colors.

# You have to paint all the posts such that no more than two adjacent fence posts have the same color.

# Return the total number of ways you can paint the fence.

# Note:
# n and k are non-negative integers.


class Solution(object):
  def numWays(self, n, k):
      """
      :type n: int
      :type k: int
      :rtype: int
      """
      if n == 0 or k == 0: return 0
      
      v = [k, 0]
        
      for i in range(1, n):
        v = [(k-1) * sum(v), 1 * v[0]]
      
      return sum(v)

