# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.lst = []
        while root:
            self.lst.append(root)
            root = root.left
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.lst) > 0

    def next(self):
        """
        :rtype: int
        """
        node = self.lst.pop()
        p = node.right
        while p:
            self.lst.append(p)
            p = p.left
        return node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())