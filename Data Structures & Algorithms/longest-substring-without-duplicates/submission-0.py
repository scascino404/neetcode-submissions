class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        max_length = 0
        seen = set()
        left, right = 0, 0
        while right < N:
            c = s[right]
            while c in seen and left < right:
                seen.remove(s[left])
                left += 1
            seen.add(c)
            right += 1
            length = right - left
            max_length = max(max_length, length)
        return max_length
