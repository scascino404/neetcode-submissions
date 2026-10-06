class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = 100
        for price in prices:
            profit = price - lowest
            max_profit = max(max_profit, profit)
            lowest = min(lowest, price)
        return max_profit