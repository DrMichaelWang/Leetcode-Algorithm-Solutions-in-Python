class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter1 = 0
        counter2 = 0
        
        for num in nums:
            if num == 1:
                counter1 += 1
                counter2 = max(counter1, counter2)
            else:
                counter1 = 0
        
        return counter2
