# Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

# Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

# You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

# Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

# Show Company Tags
# Show Tags


class Solution(object):

    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        graph = [(set(), set()) for _ in range(n)]
                
        for a in range(n):
            flag = True
            for b in range(n):
                if a == b: continue
              
                if knows(a, b):
                    graph[a][0].add(b)
                    flag = False
                    break
                else:
                    graph[a][1].add(b)
                
            if flag:
                for c in range(n):
                    if c == a: continue

                    if a in graph[c][1]:
                        flag = False
                        break
                    
                    if a in graph[c][0]:
                        continue
                    
                    if knows(c, a):
                        graph[c][0].add(b)
                    else:
                        graph[c][1].add(b)
                        flag = False
                        break
                
                if flag:
                    return a
                        
        return -1
