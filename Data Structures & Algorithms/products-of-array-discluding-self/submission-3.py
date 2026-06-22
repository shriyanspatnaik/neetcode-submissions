class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for k in range(0, len(nums)):
            i = 0
            j = len(nums) - 1
            right_product, left_product = 1, 1
            while i < k:
                left_product *= nums[i]
                i += 1
            while j > k:
                right_product *= nums[j]
                j -= 1
            product = left_product * right_product
            res.append(product)

        return res
