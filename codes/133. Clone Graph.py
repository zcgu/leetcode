# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        visit = set()
        
        if not node:
            return None
        
        root = UndirectedGraphNode(node.label)
        
        que = [node]
        table = {node.label: root}
        
        while que:
            oldNode = que.pop()
            
            if oldNode.label in visit:
                continue
            
            if oldNode.label in table:
                newNode = table[oldNode.label]
            else:
                newNode = UndirectedGraphNode(oldNode.label)
                table[oldNode.label] = newNode
            
            for oldNeighbor in oldNode.neighbors:
                if oldNeighbor.label in table:
                    newNode.neighbors.append(table[oldNeighbor.label])
                else:
                    newNeighbor = UndirectedGraphNode(oldNeighbor.label)
                    table[oldNeighbor.label] = newNeighbor
                    newNode.neighbors.append(newNeighbor)
                    
                que.append(oldNeighbor)
            
            visit.add(oldNode.label)
        
        return root
        
                    
            
            