class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxv = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxv = max(maxv, profit)
            else:
                l=r
            r+=1

        return maxv
