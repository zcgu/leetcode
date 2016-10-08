class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        
        sums = 0
        index = 0
        for i in range(len(gas)):
            sums += gas[i]
            sums -= cost[i]
            
            if sums < 0:
                sums = 0
                index = i + 1
        
        return index