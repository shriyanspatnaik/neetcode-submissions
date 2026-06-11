class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i,n in enumerate(nums):
            n2 = target - n
            if n2 in prevMap:
                return [prevMap[n2],i]
            prevMap[n] = i