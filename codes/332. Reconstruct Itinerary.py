class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if not tickets:
            return []
            
        self.n = len(tickets) + 1
        
        table = {}
        for f, e in tickets:
            table[f] = table[f] + [e] if f in table else [e]
        
        for vals in table.values():
            vals.sort()
        
        self.res = []
        
        self.dfs(['JFK'], table)
        
        return self.res
        
        
    def dfs(self, lst, table):
        # print lst
        if len(lst) == self.n:
            self.res = lst
            return True
        
        if lst[-1] not in table or not table[lst[-1]]:
            # print 1, table, lst[-1]
            return False
        
        for i in range(len(table[lst[-1]])):
            # print table
            lst.append(table[lst[-1]][i])
            del table[lst[-2]][i]
            if self.dfs(lst, table):
                return True
            table[lst[-2]].insert(i, lst[-1])
            del lst[-1]
        
        
        return False
        
        