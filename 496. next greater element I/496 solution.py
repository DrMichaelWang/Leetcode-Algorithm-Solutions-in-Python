class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for n in findNums:
            if nums.index(n)== len(nums)-1:
                result.append(-1)
            else:
                for x in nums[(nums.index(n)+1):]:
                    if x > n:
                        result.append(x)
                        break
                else:
                    result.append(-1)
                
        return result


