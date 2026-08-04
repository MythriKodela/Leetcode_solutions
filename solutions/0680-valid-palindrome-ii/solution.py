class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return True
        def ispalindrome(l,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return ispalindrome(left+1,right) or ispalindrome(left , right-1)
            left += 1
            right -= 1
        return True


        
