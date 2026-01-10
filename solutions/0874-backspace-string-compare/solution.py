class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)
        i = 0
        j = 0
        while i < len(s) :
            if s[i] == "#" :
                del s[i]
                if i > 0:
                    del s[i-1]
                    i-=1
            else: 
                i+=1

        while j < len(t) :
            if t[j] == "#" :
                del t[j]
                if j > 0 :
                    del t[j-1]
                    j-=1
            else :
                j+=1
        if len(s) != len(t) :
            return False
        
        for i in range(len(s)) :
            if s[i] != t[i] :
                return False
        return True



