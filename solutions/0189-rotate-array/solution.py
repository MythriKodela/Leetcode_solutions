class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        temp = nums[n-k:] + nums[:n-k]

        for i in range(n):
            nums[i] = temp[i]

