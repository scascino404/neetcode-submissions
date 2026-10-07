class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            middle = left + (right - left) // 2
            num = nums[middle]
            if num == target:
                return middle
            elif num < target:
                left = middle + 1
            else:
                right = middle
        return -1