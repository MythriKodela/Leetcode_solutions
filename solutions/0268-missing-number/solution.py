class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # for i in range(n+1):
        #     if i not in nums:
        #         return i
        
        val = (n*(n+1))/2
        actual_val = sum(nums)
        ans = val - actual_val
        return ans

