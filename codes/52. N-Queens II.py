class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        board = [-1 for i in range(n)]
        self.res = 0
        
        self.nextlvl(board, 0, n)
        
        return self.res
        
    def nextlvl(self, board, l, n):
        if l == n:
            self.res += 1
            return
        
        for i in range(n):
            board[l] = i
            
            flag = True
            for j in range(l):
                if board[j] == board[l] or l - j == abs(board[j] - board[l]):
                    flag = False
            
            if flag:
                self.nextlvl(board, l + 1, n)
        
        board[l] = -1