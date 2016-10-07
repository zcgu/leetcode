class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return 'Zero'
        
        lst1 = ['', "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"];
        
        lst2 = ['', "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"];
        
        lst3 = ['', "Thousand", "Million", "Billion"];
        
        count3 = 0
        res = []
        
        while num > 0:
            if num % 1000 == 0:
                count3 += 1
                num /= 1000     # 这个容易忘
                continue
            
            if count3 > 0:
                res.insert(0, lst3[count3])
                
            lower = num % 100
            if lower == 0:
                pass
            elif lower < 20:
                res.insert(0, lst1[lower])
            elif lower % 10 == 0:               # 这个容易忘
                res.insert(0, lst2[lower / 10])
            else:
                res.insert(0, lst1[lower % 10])
                res.insert(0, lst2[lower / 10])
                
            num /= 100
            
            lower = num % 10
            if lower != 0:
                res.insert(0, 'Hundred')
                res.insert(0, lst1[lower])
            
            num /= 10
            
            count3 += 1
            
        return ' '.join(res)
            
            
