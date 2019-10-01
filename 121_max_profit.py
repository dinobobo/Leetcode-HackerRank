class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mi = 0
        ma = 0
        ans = 0
        for i in range(len(prices)):
            if prices[i] < prices[mi]:
                mi = i
                ma = i
            if prices[i] > prices[ma]:
                ans = max(prices[i] - prices[mi], ans)
        return ans