from functools import cache

class Solution:
    def countBits(self, n: int) -> List[int]:
        @cache
        def count_1_bits(x):
            if x == 0:
                return 0
            return count_1_bits(x >> 1) + (x & 1)
        return [count_1_bits(x) for x in range(0, n+1)]