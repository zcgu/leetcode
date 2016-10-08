class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        
        adj = [set() for _ in range(n)]
        
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        
        leaf = [i for i in range(len(adj)) if len(adj[i]) == 1]
        
        left = n
        
        while left > 2:
            newleaf = []
            for i in leaf:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    newleaf.append(j)
            left -= len(leaf)
            leaf = newleaf
        
        return leaf