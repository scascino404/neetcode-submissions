class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_1_bits(x):
            res = 0
            while x:
                res += x & 1
                x >>= 1
            return res
        return [count_1_bits(x) for x in range(0, n+1)]