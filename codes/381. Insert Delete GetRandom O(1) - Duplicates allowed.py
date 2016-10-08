class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}
        self.lst = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.lst.append(val)
        
        if val in self.table:
            self.table[val].add(len(self.lst) - 1)
            return False
        else:
            self.table[val] = set([len(self.lst) - 1])
            return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.table or len(self.table[val]) == 0 or not self.lst:
            return False
        
        if self.lst[-1] == val:
            self.table[val].remove(len(self.lst) - 1)
            del self.lst[-1]
        else:
            index = list(self.table[val])[0]
            self.lst[index], self.lst[-1] = self.lst[-1], self.lst[index]
            
            self.table[self.lst[index]].remove(len(self.lst) - 1)
            self.table[self.lst[index]].add(index)
            
            self.table[val].remove(index)
            
            del self.lst[-1]
            
        return True
        
        
        
        
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.lst[random.randint(0, len(self.lst)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()