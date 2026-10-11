class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        can_reach = [False] * N
        can_reach[0] = True
        for i in range(N):
            if not can_reach[i]:
                continue
            for j in range(i + 1, min(i + nums[i] + 1, N)):
                can_reach[j] = True
        return can_reach[-1]