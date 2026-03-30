class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ops = []
        for i in operations:
            if i == "+":
                addition = ops[-1] + ops[-2]
                ops.append(addition)
            elif i == "D":
                product = ops[-1]
                ops.append(product*2)
            elif i == "C":
                ops.pop()
            else:
                ops.append(int(i))

        return sum(ops)
        
