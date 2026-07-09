class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        b = bin(num)[2:]
        l = ""
        for i in range(len(b)):
            l+= "1"
        integer = int(b,2)^int(l,2)
        return integer
