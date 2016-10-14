# You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

# Write a function to determine if the starting player can guarantee a win.

# For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

# Follow up:
# Derive your algorithm's runtime complexity.


class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.mem = {}
        return self.dfs(s)
    
    def dfs(self, s):
        if s in self.mem:
            return self.mem[s]

        lst = []
        
        for i in range(len(s) - 1):
            if s[i:i + 2] == '++':
                lst.append(s[:i] + '--' + s[i + 2:])
        
        if not lst:
            self.mem[s] = False
            return False
        for l in lst:
            if not self.dfs(l): 
                self.mem[s] = True
                return True
        self.mem[s] = False
        return False
        

