class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        l = []
        x = nums[:n]
        y = nums[n:]
        for i in range(n):
            l.append(x[i])
            l.append(y[i])
        return l

