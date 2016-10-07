class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        from heapq import *
        
        heap = []
        
        for i, p in enumerate(primes):
            heappush(heap, (p, [p, 0]))
        
        res = [1]
        
        for _ in range(1, n):
            while heap[0][0] <= res[-1]:
                num, pair = heappop(heap)
                
                while num <= res[-1]:
                    pair[1] += 1
                    num = pair[0] * res[pair[1]]
                
                heappush(heap, (num, pair))
            
            num, pair = heappop(heap)
            res.append(num)
            pair[1] += 1
            heappush(heap, (pair[0] * res[pair[1]], pair))
        
        return res[-1]
        
        
        
        # lst = [1]
        # indexs = [0 for i in range(len(primes))]
        
        # for pos in range(1, n):
        #     small = 2 ** 31 -1
            
        #     for i in range(len(primes)):
        #         if primes[i] * lst[indexs[i]] > lst[-1]:
        #             small = min(small, primes[i] * lst[indexs[i]])
                    
        #     lst.append(small)
        
        #     for i in range(len(primes)):
        #         while primes[i] * lst[indexs[i]] <= lst[-1]:
        #             indexs[i] += 1
                
        # return lst[-1]
        