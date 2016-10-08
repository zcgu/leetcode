class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
       
        if not board:
            return []
            
        m = len(board)
        n = len(board[0])
        res = set()
        
        def findWord(t, x ,y, visit, pre):
            if '*' in t:
                res.add(pre)
                
            if not( 0 <= x < m and 0 <= y < n and not visit[x][y]):
                return
            
            visit[x][y] = True
            
            if board[x][y] in t:
                for xx, yy in [(x - 1, y), (x + 1, y), (x, y+1), (x, y - 1)]:
                        findWord(t[board[x][y]], xx, yy, visit, pre + board[x][y])
            
            visit[x][y] = False
        
        trie = self.buildTrie(words)
        
        for x in range(m):
            for y in range(n):
                visit = [[False for _ in range(n)] for _ in range(m)]
                findWord(trie, x, y, visit, '')
        
        return list(res)


    def buildTrie(self, words):
        trie = {}
        
        for word in words:
            t =trie
            
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            
            t['*'] = '*'
        
        return trie
        
        
    
    
    