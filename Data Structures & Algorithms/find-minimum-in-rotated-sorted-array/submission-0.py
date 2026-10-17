class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = 1000
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            smallest = min(smallest, nums[mid])
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return smallest
