class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for idx, num in enumerate(nums):
            difference = target - num
            if (hashmap.get(difference, -1) >= 0):
                return [hashmap[difference], idx]
            hashmap[num] = idx
