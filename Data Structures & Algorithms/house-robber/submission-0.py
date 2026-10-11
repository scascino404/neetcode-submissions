class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        if N > 1:
            dp[1] = nums[1]
        for i in range(2, N):
            dp[i] = max(dp[:i-1]) + nums[i]
        return max(dp[-1], dp[-2]) if N > 1 else dp[-1]