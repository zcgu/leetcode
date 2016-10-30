# The API: int read4(char *buf) reads 4 characters at a time from a file.

# The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

# By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

# Note:
# The read function may be called multiple times.


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.tmp = []
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        p = 0
        while True:
            
            while self.tmp:
                if p == n:
                    return p
                buf[p] = self.tmp[0]
                del self.tmp[0]
                p += 1

            mybuf = ['' for _ in range(4)]
            readnum = read4(mybuf)
            
            if readnum == 0:
                return p
            
            for i in range(readnum):
                self.tmp.append(mybuf[i])
            
