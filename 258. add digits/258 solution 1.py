class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num//10==0:
            return num
        else:
            return self.addDigits(num%10 + num//10)
