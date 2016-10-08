class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.dfs(board)
        return
        
        
    def dfs(self, board):
        x = y = -1
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    x, y = i, j
                    break
        if x == -1:
            return True
            
        for i in range(9):
            c = chr(ord('1') + i)
            if self.valid(board, x, y, c):
                board[x][y] = c
                if self.dfs(board):
                    return True
        board[x][y] = '.'
        return False
            
    def valid(self, board, x, y, v):
        for i in range(9):
            if i != x and board[i][y] == v or i != y and board[x][i] == v:
                return False
                
        px = x / 3 * 3
        py = y / 3 * 3
        
        for i in range(3):
            for j in range(3):
                if (px + i != x or py + j != y) and board[px + i][py + j] == v:
                    return False
        
        return True