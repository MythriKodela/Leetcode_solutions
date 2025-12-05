class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers={}
        for i, num in enumerate(nums):
            diff = target - num

            if diff in numbers:
                return (i,numbers[diff])
            
            numbers[num] = i 
        return none
        
        
