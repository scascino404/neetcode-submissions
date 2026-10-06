class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zeros = 0
        prod = 1
        for num in nums:
            if num == 0:
                num_zeros += 1
            else:
                prod *= num
        
        res = [0] * len(nums)

        if num_zeros > 1:
            return res
        
        for i, num in enumerate(nums):
            if num == 0:
                res[i] = prod
            elif num_zeros == 0:
                res[i] = prod // num

        return res