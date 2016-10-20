class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda l: [-l[0], l[1]])
        
        res = []
        
        for p in people:
            res.insert(p[1], p)
        
        return res

# class Solution(object):
#     def reconstructQueue(self, people):
#         """
#         :type people: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         if not people:
#             return []
            
#         people.sort(key=lambda l: (-l[0], l[1]))
        
#         res = [people[0]]
#         people= people[1:]
        
#         while people:
#             h, count = people.pop(0)
            
#             tmpcount = 0
            
#             done = False
#             for i in range(len(res)):
#                 if tmpcount == count and res[i][0] >= h:
#                     res.insert(i, [h, count])
#                     done = True
#                     break
#                 if res[i][0] >= h:
#                     tmpcount += 1
                
#             if not done:
#                 res.append([h, count])
        
#         return res
        
        
        
        
        
    #     if not people:
    #         return []
            
    #     self.res = []
    #     self.dfs(people, [], 0)
        
    #     return self.res
        
    # def dfs(self, people, lst, pos):
    #     # print lst, pos
    #     if pos == len(people):
    #         if self.check(lst):
    #             self.res = lst
    #             return True
    #         else:
    #             return False
        
    #     pair1 = people[pos]
        
    #     if not lst:
    #         return self.dfs(people, [pair1], pos + 1)
        
    #     count = 0
    #     for i, pair2 in enumerate(lst):
    #         if count <= pair1[1]:
    #             if self.dfs(people, lst[:i] + [pair1] + lst[i:], pos + 1):
    #                 return True
                    
    #         if pair2[0] >= pair1[0]:
    #             count += 1
        
    #     if count <= pair1[1]:
    #         if self.dfs(people, lst + [pair1], pos + 1):
    #             return True
        
    #     return False
    
    # def check(self, lst):
    #     tmp = []
        
    #     from bisect import bisect_left
    #     for pair in lst:
    #         index = bisect_left(tmp, pair[0])
    #         if len(tmp) - index != pair[1]:
    #             return False
    #         tmp.insert(index, pair[0])
        
    #     return True
        
        
        
