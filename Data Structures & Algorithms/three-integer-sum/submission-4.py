class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        l = []
        for i in range(length):
            target = 0
            j = i + 1
            k = length - 1
            if nums[i-1] == nums[i] and i != 0:
                continue
            while j < k:
                addition = nums[i] + nums[j] + nums[k]
                ls = []
                if addition == target:
                    ls = [nums[i], nums[j], nums[k]]
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif addition < target:
                    j += 1
                else:
                    k -= 1
                if ls != []:
                    l.append(ls)
        return l