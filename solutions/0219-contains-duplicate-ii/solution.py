class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
       
       
        """
        i=0
        n= len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] == nums[j] and abs(i-j)<=k:
                    return True
                
        return False  

        """
        temp = set()
        for i in range(len(nums)):
            if i > k:
                temp.remove(nums[i-k-1])
            if nums[i] in temp:
                return True
            temp.add(nums[i])
            
        return False 
            

