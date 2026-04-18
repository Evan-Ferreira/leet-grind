class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        N = len(prices)
        for r in range(1, N):
            if prices[r] > prices[r - 1]:
                profit += prices[r] - prices[r - 1]
        return profit