class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result= {}
        
        for x in nums:
            if result.has_key(str(x)) is False:
                result[str(x)]=x
            else:
                del result[str(x)]
            
        return result.values()[0]
