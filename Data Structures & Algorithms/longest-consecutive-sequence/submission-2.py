class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        Max = 0
        for num in seq:
            if (num - 1) not in seq:
                cnt = 1
                while (num + cnt) in seq:
                    cnt += 1
                
                if cnt > Max:
                    Max = cnt

        return Max