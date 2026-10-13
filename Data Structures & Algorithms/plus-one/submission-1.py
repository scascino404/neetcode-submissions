class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
        if digits[0] == 0:
            digits = digits[1:]
        return digits