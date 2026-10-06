class Solution:
    def two_sum(self, nums, target, start=0):
        N = len(nums)
        seen = {}
        for i in range(start, N):
            num = nums[i]
            other = target - num
            if other in seen:
                yield True, (seen[other], i)
            seen[num] = i
        return False, (-1, -1)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        triplets = set()
        for i in range(N-2):
            for found, (j, k) in self.two_sum(nums, -nums[i], i + 1):
                if found:
                    triplets.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return [list(t) for t in triplets]