class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        secret = list(secret)
        guess = list(guess)
        
        a = 0
        b = 0
        
        for i in range(len(guess) - 1, -1, -1):
            if secret[i] == guess[i]:
                a += 1
                del secret[i]
                del guess[i]
        
        for i in range(10):
            c = chr(ord('0') + i)
            b += min(secret.count(c), guess.count(c))
        
        return str(a) + "A" + str(b) + "B"
        