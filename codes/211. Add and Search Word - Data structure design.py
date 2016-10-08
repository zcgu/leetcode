class MyNode:
    def __init__(self):
        self.table = {}

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = MyNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c in node.table:
                node = node.table[c]
            else:
                newNode = MyNode()
                node.table[c] = newNode
                node = newNode
                
        node.table['end'] = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchHelper(word, self.root)
        
    def searchHelper(self, word, node):
        if not word:
            return True if 'end' in node.table else False
            
        c = word[0]
        
        if c == '.':
            for k, n in node.table.items():
                if k != 'end' and self.searchHelper(word[1:], n):
                    return True
            return False
        else:
            return self.searchHelper(word[1:], node.table[c]) if c in node.table else False

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")