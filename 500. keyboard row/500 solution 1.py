class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a = 'QWERTYUIOP'
        b = 'ASDFGHJKL'
        c = 'ZXCVBNM'
        
        result = []
        
        for word in words:
            if set(word.upper()).issubset(a) or set(word.upper()).issubset(b) or set(word.upper()).issubset(c):
                
                result.append(word)
        
        return result
