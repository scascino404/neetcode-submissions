from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1, N2 = len(text1), len(text2)

        @cache
        def count(i, j):
            if i >= N1 or j >= N2:
                return 0
            if text1[i] == text2[j]:
                return 1 + count(i+1, j+1)
            else:
                return max(count(i+1, j), count(i, j+1))
        
        return count(0, 0)