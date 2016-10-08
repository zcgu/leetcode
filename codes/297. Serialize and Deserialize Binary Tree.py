# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        lst = []
        self.serializeHelper(root, lst)
        return ','.join(lst)
        
    def serializeHelper(self, node, lst):
        if not node:
            lst.append('None')
        else:
            lst.append(str(node.val))
            self.serializeHelper(node.left, lst)
            self.serializeHelper(node.right, lst)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        lst = data.split(',')
        return self.deserializeHelper(lst)
        
    def deserializeHelper(self, lst):
        s = lst.pop(0)
        
        if s == 'None':
            return None
        else:
            node = TreeNode(int(s))
            node.left = self.deserializeHelper(lst)
            node.right = self.deserializeHelper(lst)
            return node
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))