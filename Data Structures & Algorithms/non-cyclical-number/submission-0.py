class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False # cycle
            seen.add(n)
            digits_sq = [int(d) ** 2 for d in str(n)]
            n = sum(digits_sq)
        return True