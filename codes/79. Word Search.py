class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visit = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if self.dfs(board, visit, x, y, word, 0):
                    return True
        
        return False
    
    
    def dfs(self, board, visit, x, y, word, i):
        if i == len(word):
            return True
        
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or visit[x][y] == True\
            or board[x][y] != word[i]:
                return False
        
        visit[x][y] = True
        
        for k, j in [(-1,0), (1, 0), (0, 1), (0, -1)]:
            if self.dfs(board, visit, x+k, y+j, word, i + 1):
                return True
        
        visit[x][y] = False
        return False
        