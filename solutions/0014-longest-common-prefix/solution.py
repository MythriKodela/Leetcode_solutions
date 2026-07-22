class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
    
        # A = min(strs, key = len)
        # for s in strs:
        #     count = 0
        #     for i in range(len(A)):                  O(n^2)
        #         if A[i] == s[i]:
        #             count += 1
        #         else :
        #             break
        #     longest.append(count)
        # L = min(longest)
        # return A[:L]

        # Approach:
        # take the first word as prefix and then start checking it with others where we have startswith function to check that use it and check if yes ok else reduce the last letter and check everytime untill it matches and then if that matches make it as prefix and continue this process for all the words and retur the remaining prefix.
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
            if not prefix :
                return ""
        return prefix
                

