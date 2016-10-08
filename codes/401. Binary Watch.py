class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for i in range(num + 1):
            hs = self.hour(i)
            ms = self.minute(num-i)
            
            for h in hs:
                for m in ms:
                    if len(m) < 2:
                        m = '0' + m
                    res.append(h + ':' + m)
        res.sort()
        return res
        
        
        
    def hour(self, num):
        if num > 4:
            return []

        self.hours = []
        self.find(num, 4, 0)
        return self.hours
        
    def find(self, num, pos, time):
        if num == 0:
            if time <= 11:
                self.hours.append(str(time))
            return
        if pos < 0:
            return
        
        self.find(num, pos-1, time)
        self.find(num-1, pos-1, time+ 2** pos)
        
    
    def minute(self, num):
        if num > 6:
            return []
            
        self.minutes = []
        self.findm(num, 6, 0)
        return self.minutes
        
    def findm(self, num, pos, time):
        if num == 0:
            if time <= 59:
                self.minutes.append(str(time))
            return
        if pos < 0:
            return
        
        self.findm(num, pos-1, time)
        self.findm(num-1, pos-1, time + 2** pos)
        
        