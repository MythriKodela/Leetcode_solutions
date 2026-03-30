class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            else:
                profit = prices[i] - min_price
                max_profit = max(max_profit , profit)
        return max_profit


