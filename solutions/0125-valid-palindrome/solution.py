import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub(r"[^a-z0-9]", "", s)
        n= len(s)
        i= 0
        j= n-1
        for i in range(n):
            if s[i] != s[j]:
                return False
            else:
                j-=1
        return True
        
