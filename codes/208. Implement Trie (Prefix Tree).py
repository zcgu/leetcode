class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c in node.table:
                node = node.table[c]
            else:
                newNode = TrieNode()
                node.table[c] = newNode
                node = newNode
        node.table['0'] = None
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        
        for c in word:
            if not node or not node.table or c not in node.table:
                return False
            node = node.table[c]
        
        return '0' in node.table
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        
        for c in prefix:
            if not node or not node.table or c not in node.table:
                return False
            node = node.table[c]

        return True
# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")