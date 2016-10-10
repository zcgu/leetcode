# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# For example:

# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

# Show Hint 
# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# Show Company Tags
# Show Tags
# Show Similar Problems


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = [set() for _ in range(n)]
        
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        
        visited = [0 for _ in range(n)]
        
        if not self.dfs(graph, visited, 0, None):
            return False
        
        if 0 in visited:
            return False
        
        return True
        
        
    def dfs(self, graph, visited, n, last):         # 加一个last就不back了，interesting.
        if visited[n] == -1:
            return False
        
        visited[n] = -1
        
        for i in graph[n]:
            if last is not None and i == last:
                continue
            if not self.dfs(graph, visited, i, n):
                return False
        
        return True
        
        
        
