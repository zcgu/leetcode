class Solution(object):
    def canFinish(self, numCourses, p):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not p:
            return True
        
        graph = [set() for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        
        for a, b in p:
            graph[a].add(b)
        
        for i in range(numCourses):
            if self.dfs(graph, visit, i):
                return False                # False no.
        
        return True
    
    def dfs(self, graph, visit, node):  # -1 being visit, 1 already visit. True have circle.
        if visit[node] == -1:
            return True
        if visit[node] == 1:
            return False
        
        visit[node] = -1
        for pre in graph[node]:
            if self.dfs(graph, visit, pre):
                return True
        visit[node] = 1
        return False
        
        