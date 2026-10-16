class Solution:
    def binary_search(self, nums, target, start=0):
        left = start
        right = len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True, mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False, None

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            found, j = self.binary_search(nums, target - num, start=i+1)
            if found:
                return [i+1, j+1]
        assert False # unreachable