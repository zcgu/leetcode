class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1. 如果碰到成对的，用')'减去'('左边的更新。
        res = 0
        stack = []
        p = 0
        
        while p < len(s):
            if s[p] == '(':
                stack.append([s[p], p])
            else:
                if stack and stack[-1][0] == '(':
                    c, index = stack.pop()
                    if not stack:
                        res = max(res, p + 1)
                    else:
                        res = max(res, p - stack[-1][1])
                else:
                    stack.append([s[p], p])
            p += 1
        
        return res
        
        
        
        # 2. 记不住这是什么了
        # stack = []
        
        # for i, c in enumerate(s):
        #     if c == '(':
        #         stack.append([i, c])
        #     else:
        #         if not stack or stack[-1][1] == ')':
        #             stack.append([i, c])
        #         else:
        #             stack.pop()
        
        # if not stack:
        #     return len(s)
        # print stack
        # start = -1  # interesting -1
        # res = 0
        # for i, c in stack:
        #     res = max(res, i - start - 1)
            
        #     start = i
        # res = max(res, len(s) - start - 1)  #don't forget
        # return res
            
            