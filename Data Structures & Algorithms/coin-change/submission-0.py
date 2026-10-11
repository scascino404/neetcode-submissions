class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 10 ** 5

        dp = [INF] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for coin in coins:
                if (j := i - coin) >= 0:
                    dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[amount] if dp[amount] != INF else -1