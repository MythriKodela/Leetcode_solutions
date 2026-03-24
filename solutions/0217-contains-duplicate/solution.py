class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for a in nums:
            if a in seen:
                return True
            else:
                seen.add(a)
        return False
