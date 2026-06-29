class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        Max = 0
        for num in seq:
            if (num - 1) not in seq:
                cnt = 1
                while (num + 1) in seq:
                    cnt += 1
                    num += 1
                
                if cnt > Max:
                    Max = cnt

        return Max