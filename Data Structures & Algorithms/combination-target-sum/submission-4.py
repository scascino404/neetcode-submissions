class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)

        combinations = []
        seen = set()
        def backtrack(idx, total=0, combination=()):
            if idx >= N or total > target:
                return

            if (idx, total, combination) in seen:
                return

            if total == target:
                combinations.append(combination)
                return

            backtrack(idx+1, total, combination)

            new_total = total + nums[idx]
            new_combination = combination + (nums[idx],)

            backtrack(idx,   new_total, new_combination)
            backtrack(idx+1, new_total, new_combination)

            seen.add((idx, total, combination))

        backtrack(0)
        
        return [list(c) for c in set(combinations)]