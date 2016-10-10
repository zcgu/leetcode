# The API: int read4(char *buf) reads 4 characters at a time from a file.

# The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

# By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

# Note:
# The read function may be called multiple times.


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    tmp = ['' for _ in range(4)]
    index = 0
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        
        tmp = self.tmp
        total = 0
        
        if n <= self.index:
            buf[total:total+ n] = self.tmp[:n]
            self.tmp[:self.index - n] = self.tmp[n: self.index]
            self.index -= n
            return n
        else:
            buf[total:total+self.index] = self.tmp[:self.index]
            total += self.index
            n -= self.index
            self.index = 0
        
        for _ in range(n / 4):
            num = read4(tmp)
            
            if num < 4:
                buf[total:total+num] = tmp[:num]
                self.index = 0
                return total + num
            else:
                buf[total:total + 4] = tmp[:4]
                total += 4
        
        if n % 4 != 0:
            num = read4(tmp)
            
            if num <= n % 4:
                buf[total:total + num] = tmp[:num]
                self.index = 0
                return total + num
            else:
                buf[total:total + n % 4] = tmp[:n % 4]
                tmp[:num - n%4] = tmp[n%4: num]
                self.index = num - n % 4
                return total + n % 4
        else:
            self.index = 0
            return total
            
            
            
