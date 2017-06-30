class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_sort = sorted(nums)
        n = len(nums)  
        first_half = []
        second_half = []
        for x in range(n):
            if x%2==0:
                first_half.append(num_sort[x])
            else: 
                second_half.append(num_sort[x])
        pairs= zip(first_half, second_half)
        total = 0
        for a in pairs:
            total = total + min(a)
        return total
