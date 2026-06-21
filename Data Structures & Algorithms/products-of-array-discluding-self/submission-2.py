class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        f = 0
        for n in nums:
            if n != 0:
                prod *= n
            else:
                f += 1
        
        l = []
        for n in nums:
            if (f >= 1 and n != 0) or (len(nums) - f == 0) or (f >= 2):
                l.append(0)
            elif f >= 1 and n == 0:
                l.append(prod)
            else:
                l.append(int(prod/n))
        return l