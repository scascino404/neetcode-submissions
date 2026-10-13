class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        i = 31
        while n:
            bit = n & 1
            rev |= bit << i
            i -= 1
            n >>= 1
        return rev