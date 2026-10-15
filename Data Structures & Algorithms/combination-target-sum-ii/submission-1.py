class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums = list(sorted(filter(lambda num: num <= target, nums)))
        N = len(nums)

        combinations = []
        seen = set()
        def backtrack(idx, total=0, combination=()):
            if total == target:
                combinations.append(combination)
                return

            if idx >= N or \
               total > target or \
               (idx, total, combination) in seen:
                return

            backtrack(idx+1, total, combination)
            backtrack(idx+1, total + nums[idx], combination + (nums[idx],))

            seen.add((idx, total, combination))

        backtrack(0)

        return [list(c) for c in set(combinations)]