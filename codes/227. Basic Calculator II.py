class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '')
        
        que = []
        
        i = 0
        
        while i < len(s):
            if s[i] == '+' or s[i] == '-':
                self.cal(que)
                que.append(s[i])
                i += 1
            elif s[i] == '*' or s[i] == '/':
                que.append(s[i])
                i += 1
            else:
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                num = int(s[start:i])
                
                if not que or que[-1] == '+' or que[-1] == '-':
                    que.append(num)
                else:
                    sign = que.pop()
                    num1 = que.pop()
                    
                    que.append(num1 * num if sign == '*' else num1 / num)
        
        self.cal(que)
        return que[0]
        
    def cal(self, que):
        
        while len(que) > 1:
            num1 = que.pop(0)
            sign = que.pop(0)
            num2 = que.pop(0)
            
            r = num1 + num2 if sign == '+' else num1 - num2
            
            que.insert(0, r)
        
        
        
                