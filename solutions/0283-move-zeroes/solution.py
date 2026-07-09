class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 1
        n = len(nums)
        # while i <= n and j<=n:
        #     if nums[i] == 0:
        #         if j==n and nums[j]==0:
        #             break
        #         while nums[j] == 0 and j+1<=n:
        #             j += 1

        #         nums[i],nums[j] = nums[j],nums[i]
        #     else:
        #         i += 1
        #         j+=1
        # return nums
        
        for i in range(n):
            if nums[i] == 0:
                if j>=n:
                    break
                while nums[j] == 0 and j+1<n:
                    j += 1
                nums[i], nums[j] = nums[j],nums[i]
                j += 1
            else:
                j=i+1
        return nums


        
