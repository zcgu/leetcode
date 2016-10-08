class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if numCourses == 0:
            return []
        
        graph = [set() for _ in range(numCourses)]
        
        visit = [0 for _ in range(numCourses)]
        
        for p1, p2 in prerequisites:
            graph[p1].add(p2)
        
        self.res = []
        
        for i in range(numCourses):
            if not self.dfs(graph, visit, i):
                return []
        
        return self.res
    
    def dfs(self, graph, visit, i):
        if visit[i] == 1:
            return True
        if visit[i] == -1:
            return False
            
        visit[i] = -1
        
        for j in graph[i]:
            if not self.dfs(graph, visit, j):
                return False
        
        self.res.append(i)
        
        visit[i] = 1
        
        return True
        
        
        
        
        
        
        
    