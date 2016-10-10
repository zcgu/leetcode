# The API: int read4(char *buf) reads 4 characters at a time from a file.

# The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

# By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

# Note:
# The read function will only be called once for each test case.

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        # 这个buffer啊。。。。是一个buffer pool，不是直接append。
        
        total = 0
        for _ in range(n / 4):
            tmp = ['' for _ in range(4)]
            num = read4(tmp)
            buf[total:total+num] = tmp[:num]
            
            if num < 4:
                return total + num
            else:
                total += 4
        
        
        if n % 4 != 0:
            tmp = ['' for _ in range(4)]
            num = read4(tmp)
            
            if num > n % 4:
                buf[total:total+n%4] = tmp[:n % 4]
                return n
            else:
                buf[total:total+num] = tmp[:num]
                return total + num
        else:
            return n
        
        
        
        
