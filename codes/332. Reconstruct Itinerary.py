class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        tickets.sort()
        return self.dfs(['JFK'], tickets)
        
        
    def dfs(self, lst, tickets):
        if not tickets:
            return lst
            
        for i, t in enumerate(tickets):
            if t[0] == lst[-1]:
                res = self.dfs(lst + [t[1]], tickets[:i] + tickets[i+1:])
                if res:
                    return res
        return None
