class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        majority = {}
        for num in nums:
            if num in majority:
                majority[num] += 1
            else:
                majority[num] = 1
            if majority[num] > n//2:
                return num


