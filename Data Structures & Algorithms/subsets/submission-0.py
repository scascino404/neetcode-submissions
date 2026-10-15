class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)

        subsets = [[]]
        def backtrack(idx, subset=[]):
            if idx >= N:
                return

            new_subset = subset + [nums[idx]]
            subsets.append(new_subset)

            backtrack(idx+1, subset)     # take
            backtrack(idx+1, new_subset) # don't take
        
        backtrack(0)

        return subsets