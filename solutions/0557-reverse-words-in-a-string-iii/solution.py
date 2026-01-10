class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        n = len(s)
        i = 0
        j = 0
        while j < n :
            while j < n and s[j] != " ":
                j+=1
            k = j-1
            while i < k :
                s[i] , s[k] = s[k] , s[i]
                i+=1
                k-=1
            j+=1
            i = j
        return "".join(s)    

        
