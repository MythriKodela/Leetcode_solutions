class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i=0
        new_string = ""
        n1 = len(word1)
        n2 = len(word2)
        n = min(n1 , n2)
        for i in range(n):
            new_string += word1[i] + word2[i]
        if n1>n2:
            new_string += word1[n:]
        else:
            new_string += word2[n:]
        return new_string
        
