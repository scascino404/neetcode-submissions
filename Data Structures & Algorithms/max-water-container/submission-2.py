class Solution:
    def maxArea(self, heights: List[int]) -> int:
        N = len(heights)

        max_area = 0
        left, right = 0, N-1
        while left < right:
            base = right - left
            height = min(heights[left], heights[right])
            area = base * height
            max_area = max(max_area, area)

            if heights[left] <= heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1

        return max_area

