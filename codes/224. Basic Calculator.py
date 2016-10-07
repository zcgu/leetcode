class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 这个题，在遇到数字的时候做处理，遇到右括号去掉que[-2]就行了。

        stack = []
        s = s.replace(' ', '')
        
        p = 0
        
        while p < len(s):
            if s[p].isdigit():
                start = p
                while p < len(s) and s[p].isdigit():
                    p += 1
                stack.append(int(s[start:p]))
                self.cal(stack)
            elif s[p] == '(':
                stack.append('(')
                p += 1
            elif s[p] in ['+', '-']:
                stack.append(s[p])
                p += 1
            else:
                del stack[-2]
                self.cal(stack)
                p += 1
        self.cal(stack)
        return stack[0]
                
                
    def cal(self, stack):
        while len(stack) > 1 and stack[-2] != '(':
            
            num2 = stack.pop()
            sign = stack.pop()
            num1 = stack.pop()
            
            stack.append(num1 + num2 if sign == '+' else num1 - num2)
            
            
            
                
                
                
                