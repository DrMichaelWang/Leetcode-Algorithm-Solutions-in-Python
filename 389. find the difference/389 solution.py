class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # sort the two strings and create two lists:
        s1=sorted(s)
        t1=sorted(t)
        
        # remove the element in s1 one by one in t1, the left one is the different/new element:
        for elem in s1:
            t1.remove(elem)
        return t1[0]
        
